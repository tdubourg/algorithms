/***
Author: TD
License: GPLv3
***/

#include "stdio.h"
#include "stdlib.h"
#include "time.h"
#include "math.h"

#define PRINT_VALUES

#ifndef ITERATIONS
#define ITERATIONS 15
#endif

#ifndef POWER
#define POWER 1
#endif

#ifndef LEFT
#define LEFT(i) (2*i+1)
#endif

#ifndef RIGHT
#define RIGHT(i) (2*i+2)
#endif

#ifndef PARENT
#define PARENT(i) ((i-1)/2) // int division = floor() 
#endif

typedef int heap_element;

typedef struct heap_t {
	int sz;
	int capacity;
	heap_element* elements;
} heap;

heap* create_heap(int sz) {
	heap* h = (heap*)malloc(sizeof(heap));
	h->elements = (heap_element*)malloc(sizeof(heap_element) * 2 * sz);
	h->sz = 0;
	h->capacity = sz;
	
	return h;
}


heap* swap(heap* h, int i, int j) {
#ifdef DBG
	printf("swap entering i=%d, j=%d\n", i, j);
	printf("el[i]=%d, el[j]=%d\n", h->elements[i], h->elements[j]);
#endif
	
	heap_element tmp = h->elements[i];
	
	h->elements[i] = h->elements[j];
	h->elements[j] = tmp;
	
#ifdef DBG
	printf("swap exiting i=%d, j=%d\n", i, j);
	printf("el[i]=%d, el[j]=%d\n", h->elements[i], h->elements[j]);
#endif
	return h;
}


heap* increase_key(heap* h, int i, heap_element val) {
	
	if (i >= h->sz)
	{
		return h;
	}
	
	if (val < h->elements[i])
	{
		printf("Tried to run increase_key() for decreasing a key. Tried: %d -> %d.\n", h->elements[i], val);
		return h;
	}
	
	h->elements[i] = val;
	while(i > 0 && h->elements[PARENT(i)] < val) {
		h = swap(h, PARENT(i), i);
		i = PARENT(i);
	}
	
	return h;
}


heap* insert_heap(heap* h, heap_element e) {
	static int mini = -1;
	
	if (h->sz >= h->capacity)
	{
		printf("Max capacity reached");
		return h;
	}
	
	if(e < mini) {
		mini = e;
	}
	
	int key = mini - 1; // Faking - infinity : Always less than anything else in the heap!
	
	h->sz++;
	h->elements[h->sz-1] = key;
	increase_key(h, h->sz-1, e);// Set the real key value
	
	return h;
}

heap* max_heap_ify(heap* h, int i) {
#ifdef DBG
	printf("max_heap_ify entering i=%d\n", i);
#endif
	int l = LEFT(i);
	int r = RIGHT(i);
	
	int sz = h->sz;
	int largest = -1;
	
	heap_element* els = h->elements;
	
	if (l < sz && els[l] > els[i])
	{
		largest = l;
	} else {
		largest = i;
	}
	
	if (r < sz && els[r] > els[largest])
	{
		largest = r;
	}
	
	if (largest != i)
	{
		h = swap(h, i, largest);
		h = max_heap_ify(h, largest); 	// Don't be fooled, largest is the INDEX of the formerly-largest, thus in case of swap it is the index of a CHILD
										// As we've just taken DOWN the parent, we in fact relaunch max-heapify on the PARENT in order to see if we can take it EVEN MORE DOWN
	}
	
#ifdef DBG
	printf("max_heap_ify returning\n");
#endif

	return h;
}

heap_element heap_pop(heap* h) {
	heap_element e = h->elements[0];
	
	swap(h, 0, h->sz-1);
	h->sz--;
	max_heap_ify(h, 0);
	
	return e;
}

heap* build_heap(heap* h) {
	for (int i = h->sz / 2; i >= 0; i--)
	{
		max_heap_ify(h, i);
	}
	return h;
}

heap* heap_sort(heap* h) {
	for (int i = h->sz - 1; i >= 1; --i)
	{
		swap(h, 0, i);
		h->sz--;
		max_heap_ify(h, 0);
	}
	return h;
}

void _printheap(int j, heap* h, int node) {
	for (int i = 0; i < j; ++i)
	{
		printf("\t");
	}
	printf("- %d\n", h->elements[node]);
	
	if (LEFT(node) < h->sz)
	{
		_printheap(j+1, h, LEFT(node));
	}
	if (RIGHT(node) < h->sz)
	{
		_printheap(j+1, h, RIGHT(node));
	}
	

}

void printheap(heap* h) {
	printf("\n");
	_printheap(0, h, 0);
	printf("\n");
}

int main(int argc, char const *argv[])
{
	// Generating random values: 
	srand ( time(NULL) );
	
	for (int j = 0; j < POWER; ++j)
	{
		int n = ITERATIONS * (int)pow(10, j);
		printf("Beginning for %d iterations", n);
		printf("\n");
		
		heap* h = create_heap(n);
		heap_element values[n];
		
		printf("Generating the values...(power=%d)\n", j);
		int sign = -1;
		for (int i = 0; i < n; ++i)
		{
			sign = sign * (-1);
			values[i] = sign * rand() % (n*10);
		}
		
#ifdef PRINT_VALUES
		printf("Elements un-sorted: \n");
		for (int i = 0; i < n; ++i)
		{
			printf("%d\t", values[i]);
		}
#endif	
		
		printf("\nBuilding the heap...\n");
		int a = clock();
		
		// h = build_heap(h);
		
// #ifdef PRINT_VALUES
// 		printf("Elements un-sorted but heap built: \n");
		
// 		for (int i = 0; i < n; ++i) {
// 			printf("%d\t", i);
// 		}
		
// 		printf("\n");
		
// 		for (int i = 0; i < n; ++i)
// 		{
// 			printf("%d\t", h->elements[i]);
// 		}
// #endif
		// 
		// h = heap_sort(h);
		for (int i = 0; i < n; ++i)
		{
			insert_heap(h, values[i]);
		}
		int b = clock();
		
// #ifdef PRINT_VALUES
// 		printf("\nElements sorted: \n");
// 		for (int i = 0; i < n; ++i)
// 		{
// 			printf("%d\t", h->elements[i]);
// 		}
// #endif
		
#ifdef PRINT_VALUES
		printf("\nHeap content:\n");
		for (int i = 0; i < n; ++i)
		{
			printf("%d\t", h->elements[i]);
		}
		printheap(h);
		
		printf("\nPriority queue:\n");
		for (int i = 0; i < n; ++i)
		{
			printf("%d\t", heap_pop(h));
		}
#endif
		
		free(h->elements);
		free(h);
		
		printf("\nTime for %d iterations=%f\n", ITERATIONS, ((float)(b-a)/(float)CLOCKS_PER_SEC));
	}
	
	return 0;
}