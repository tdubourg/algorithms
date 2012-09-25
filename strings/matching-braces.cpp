/***
Author: TD
License: GPLv3
Microsoft Ireland 2012 Internship Application Form Coding Question
Problem statement: check if all the braces (including parenthesis, curly brackets and angle brackets) 
are correctly closed (in the right order... intuitively: just a syntax checking)
***/

#include <vector>
#include <iostream>
using namespace std;
int checkBraces(char* s) {
	vector<char> stack;
	for (int i = 0; s[i] != '\0'; i++) {
		if (s[i] == '{' || s[i] == '(' || s[i] == '[') {
			stack.push_back(s[i]);
		} else if (s[i] == '}') {
			if (stack.size() > 0 && stack.back() != '{') {
				return 0;
			} else {
				stack.pop_back();
			}
		} else if (s[i] == ']') {
			if (stack.size() > 0 && stack.back() != '[') {
				return 0;
			} else {
				stack.pop_back();
			}
		} else if (s[i] == ')') {
			if (stack.size() > 0 && stack.back() != '(') {
				return 0;
			} else {
				stack.pop_back();
			}
		}
	}
	if(stack.size() > 0) {
		return 0;
	}
	return 1;
}
