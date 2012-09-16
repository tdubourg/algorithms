#include "stdlib.h"
#include "stdio.h"
#include "string.h"

int pow(int a, unsigned int exp) {

	if (0 == exp)
	{
		return 1;
	}

	int res = a;
	int i=1;
	for (; i < exp; ++i)
	{
		res *= a;
	}

	return res;
}

char* itoa(int i) {
	unsigned int n, x, start; // beware, unsigned and signed are not comparable between each other, these two should be used only with themselves
	int comp, divider, ord0;
	char* res;

	n = 0;

	if(0 == i) {
		res = malloc(sizeof(char)*1);
		res[0] = '0';
		return res;
	}
	
	if(i > 0) {
		comp = 1;
		while(i >= comp) {
			n += 1;
			comp *= 10;
		}
	}
	else {
		comp = -1;
		while(i <= comp) {
			n += 1;
			comp *= 10;
		}
	}

	n -= 1; // Because we do >= and <= comparisons then we need to substract one BUT it avoids thinking about "is i beginning with a 1? With a 9?" Here we are sure we were at the next power of ten and we substract one
	
	// We now have the length of the number in n
	start = 0;
	if(i < 0) {
		res = malloc(sizeof(char)*(n+2));// +1 for the - sign
		res[0] = '-';
		start = 1;
		i *= -1;
	}
	else {
		res = malloc(sizeof(char)*(n+1));
	}

	divider = pow(10, n);
	ord0 = '0';
	// printf("n=%d\n", n);
	for(x=start; x <= (start+n); x++) {
		// printf("i=%d\n", i);
		// printf("divider=%d\n", divider);
		res[x] = (char) (i/divider + ord0);
		int tmp = i/divider; // IS NOT equal to x, will floor() in the middle...
		// printf("tmp=%d\n", tmp);
		i -= tmp * divider;
		divider /= 10;
	}
	res[start+n+1] = '\0';
	return res;
}

int main(int argc, char const *argv[])
{
	printf("Please write a number\n");
	int a;
	scanf("%d", &a);
	printf("%s\n", itoa(a));

	return 0;
}

