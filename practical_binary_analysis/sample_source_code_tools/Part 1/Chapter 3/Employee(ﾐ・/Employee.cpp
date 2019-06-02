
#include "windows.h"
#include "stdio.h"
#include "tchar.h"

class Employee
{
	public :
		int number;
		char name[128];
		long pay;
		void ShowData();
		void Test();
};

void Employee::ShowData()
{
	printf("number: %d\n", number);
	printf("name: %s\n", name);
	printf("pay: %d\n", pay);
	Test();

	return;
}

void Employee::Test()
{
	printf("Test fuction\n");
	return;
}

// Employee kang;
int main(int argc, char* argv[])
{
	Employee yamamoto;
	
	printf("size: %X\n", sizeof(Employee));
	
	yamamoto.number = 0x1111;
	_tcscpy(yamamoto.name, _T("ŽR–{‘¾˜Y"));
	yamamoto.pay = 0x100;
	yamamoto.ShowData();
	return 0;
}
