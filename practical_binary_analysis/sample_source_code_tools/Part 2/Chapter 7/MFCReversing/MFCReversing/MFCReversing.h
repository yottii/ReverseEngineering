
// MFCReversing.h : PROJECT_NAME アプリケーションのメイン ヘッダー ファイルです。
//

#pragma once

#ifndef __AFXWIN_H__
	#error "PCH に対してこのファイルをインクルードする前に 'stdafx.h' をインクルードしてください"
#endif

#include "resource.h"		// メイン シンボル


// CMFCReversingApp:
// このクラスの実装については、MFCReversing.cpp を参照してください。
//

class CMFCReversingApp : public CWinApp
{
public:
	CMFCReversingApp();

// オーバーライド
public:
	virtual BOOL InitInstance();

// 実装

	DECLARE_MESSAGE_MAP()
};

extern CMFCReversingApp theApp;