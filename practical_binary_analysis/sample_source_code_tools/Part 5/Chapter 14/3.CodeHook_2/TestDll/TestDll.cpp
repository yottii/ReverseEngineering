#include <windows.h>
#include "stdio.h"
#include <tchar.h>
#include <tlhelp32.h>
#include <Psapi.h>
#include "TestDll.h"
#include "TraceBC.h"

#pragma comment(linker, "/base:0x33300000 /fixed" )

typedef void (__cdecl *TPseudoSend)(int, char *, int);
TPseudoSend lpPseudoFunc;

char *g_buf = NULL;
int g_len = 0;

__declspec(naked) int HookSend()
{
	__asm
	{
		push ebx
		push eax
		push edx
		mov ebx, [ebp+0x10]
		mov eax, [ebp+0xC]
		mov edx, [ebp+0x4]
		push ebx
		push eax
		push edx
		call lpPseudoFunc
		add esp, 0xc
		pop edx
		pop eax
		pop ebx
		mov eax, 0x719E4C43
		jmp eax
	}
}

void PseudoFunc(int retaddr, char *buf, int len)
{
	if (len != 1 && len > 0)
	{
		//TRACEB("[%x] send : [%d]", retaddr, len);

		int len_temp = 0;
		int len_temp2 = 0;
		char szMsg1[MAX_PATH] = {0,};
		char szMsg2[MAX_PATH] = {0,};
		for (int i=0; i<len; ++i)
		{
			if (MAX_PATH < i)
				break;

			if (buf[len_temp] == '\0')
				len_temp += sprintf(szMsg1 + len_temp, "_");
			else
				len_temp += sprintf(szMsg1 + len_temp, "%c", buf[i]);
			
			// 200 バイト以上は無視する
			if (len_temp2 < 200)
				len_temp2 += sprintf(szMsg2 + len_temp2, "%02X ", *(buf + i));
		}
		
		TRACEB("[%x] send : [%d] %s", retaddr, len, szMsg1);
		TRACEB("     dump : %s", szMsg2);
	}
}

void InitHooking2()
{
	lpPseudoFunc = PseudoFunc;

	typedef void (WINAPI *Tsend)(SOCKET, const char *, int, int);
	Tsend fnsend;

	TCHAR szWs2_32Dll[MAX_PATH];
	GetSystemDirectory(szWs2_32Dll, MAX_PATH);
	_tcscat(szWs2_32Dll, _T("\\ws2_32.dll"));
	HMODULE hMod = LoadLibrary(szWs2_32Dll);
	fnsend = (Tsend)GetProcAddress(hMod, "send");

	//719E4C3D                          0F84 256A0000              je ws2_32.719EB668
	//719E4C3D をフックする
	LPVOID lpTargetAdr = (LPVOID)((DWORD)fnsend + 0x16);

	TRACEB(_T("lpTargetAdr: %x"), lpTargetAdr);
	DWORD dwOldProtect = 0;
	VirtualProtect(lpTargetAdr, 6, PAGE_READWRITE, &dwOldProtect);
	
	// こんなハードコーディングはしない
	/*
	//719E4C3D                        - E9 BEC3619E              jmp btmmhook.10001000
	//719E4C42                          90                       nop

	//719E4C3D         - E9 BEC391C1     jmp 33301000
	//719E4C42           90              nop
	*((LPBYTE)lpTargetAdr + 0) = 0xE9;
	*((LPBYTE)lpTargetAdr + 1) = 0xBE;
	*((LPBYTE)lpTargetAdr + 2) = 0xC3;
	*((LPBYTE)lpTargetAdr + 3) = 0x91;
	*((LPBYTE)lpTargetAdr + 4) = 0xC1;
	*((LPBYTE)lpTargetAdr + 5) = 0x90;
	*/

	//新しいルール!!!
	//これを入れたい jmp 33301000
	//でも、 33301000 を知らない(関数名では知っている HookSend)
	//HookSend - フックする箇所 - 5 = 入れるべき値
	//HookSend - send - 0x16 - 5 ここに辿りつく
	// 0x16 は send からその分後ろにあるもの
	// 5 は  5 byte 損する
	*((LPBYTE)lpTargetAdr + 0) = 0xE9;
	DWORD dwBufferAdr = (DWORD)HookSend - (DWORD)fnsend - 0x16 - 5;	
	*((LPDWORD)((LPBYTE)lpTargetAdr + 1)) = dwBufferAdr;
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
	if (fdwReason == DLL_PROCESS_ATTACH)
	{
		DisableThreadLibraryCalls((HMODULE)hinstDLL);
		InitHooking2();
	}
	else if (fdwReason == DLL_PROCESS_DETACH)
	{
	}

	return TRUE;
}