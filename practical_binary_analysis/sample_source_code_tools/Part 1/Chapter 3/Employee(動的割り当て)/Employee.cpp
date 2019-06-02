
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

int main(int argc, char* argv[])
{
	Employee *pYamamoto;	
	pYamamoto = new Employee;

	pYamamoto->number = 0x1111;
	_tcscpy(pYamamoto->name, _T("ŽR–{‘¾˜Y"));
	pYamamoto->pay = 0x100;

	pYamamoto->ShowData();

	delete pYamamoto;
	
	return 0;
}
