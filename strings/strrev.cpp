/***
Author: TD
License: GPLv3
***/

#include "iostream"
#include "string"
#include "string.h"

using namespace std;
void strrev(char* str) {
	// cout << "Received: " << str << endl;
	char* start = str;
	
	while(*(++str));
	// cout << "Remaining: " << (int) *str << endl;
	
	char* m = (str - start) / 2 + start;
	// cout << "Length " << (int)m << endl;
	while(start <= m) {
		char c = *start;
		*start = *(--str);
		*str = c;
		start++;
	}
}


int main(int argc, char const *argv[])
{
	string str;
	cin >> str;
	int l = str.length();
	char buff[l+2];
	strcpy(buff, str.c_str());
	buff[l+1] = 0;
	cout << "You typed : " << buff << endl;
	strrev(buff);
	cout << "Reversed:" << buff << endl;
	
	int a = 1;
	int b = 2;
	cout << a << b << endl;
	a ^= b;
	b ^= a;
	a ^= b;
	cout << a << b << endl;

/** This is a benchmark to see if there is any differences between 
various ways of swapping the values of 2 variables.
The question cames to me when implementing the loop of strrev() 
so I decided to figure it out. This code has nothing to do
with the implentation of strrev() itself. **/
#define MAX 3000000000
	
	for (int j = 0; j < 4; ++j)
	{
		int t1 = clock();
		for (int i = 0; i < MAX; ++i)
		{
			int c = a;
			a = b;
			b = a;
		}
		int t2 = clock();
		
		cout << "Done in " << ((float)(t2-t1)/(float)CLOCKS_PER_SEC) << "s" << endl;
		
		t1 = clock();
		int c;
		for (int i = 0; i < MAX; ++i)
		{
			c = a;
			a = b;
			b = a;
		}
		t2 = clock();	
		
		cout << "Done in " << ((float)(t2-t1)/(float)CLOCKS_PER_SEC) << "s" << endl;
		
		t1 = clock();
		for (int i = 0; i < MAX; ++i)
		{
			a ^= b;
			b ^= a;
			a ^= b;
		}
		t2 = clock();
		cout << "Done in " << ((float)(t2-t1)/(float)CLOCKS_PER_SEC) << "s" << endl;
		
		t1 = clock();
		for (int i = 0; i < MAX; ++i)
		{
			register int c1 = a;
			a = b;
			b = a;
		}
		t2 = clock();
		cout << "Done in " << ((float)(t2-t1)/(float)CLOCKS_PER_SEC) << "s" << endl;
		
		t1 = clock();
		register int c1;
		for (int i = 0; i < MAX; ++i)
		{
			c1 = a;
			a = b;
			b = a;
		}
		t2 = clock();
		cout << "Done in " << ((float)(t2-t1)/(float)CLOCKS_PER_SEC) << "s" << endl;

		
		cout << endl;
	}	
	
	return 0;
}