#include "unionfind.h"

unionfind:: unionfind(int n)
{
 size = n;
 p = new int[size];
 for (int i = 0; i<size; i++) p[i] = i; // p[i]==i  stands for "no parent"
}

void unionfind::unions(int i, int j)
//unites sets rooted at i and j making j the root, i not equal to j
{
 p[i] = j;
}

int unionfind::find(int i)
//find the root (representative) of the set containing i
{
	while (p[i] != i) i = p[i];
	return i;
}

