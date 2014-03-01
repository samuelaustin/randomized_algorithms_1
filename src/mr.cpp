#include <iostream>
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <omp.h>
//#include "util.cpp"

using namespace std;

int modPow(int a, int b, int c)
{
	int res = 1;
	for(int i = 0; i < b; i++)
	{
		res *= a;
		res = res % c;
	}
	return res % c;
}

bool mr(int n, int it)
{
	if(n == 2 || n == 3) return true;

	if(n < 2 || (n != 2 && n%2==0)) return false;
	
	srand((unsigned)time(0));

	int s = n-1;
	while(s%2 == 0)
		s = s/2;
	
	bool ans = true;
	//#pragma omp parallel for
	for(int i = 0; i < it & ans; i++)
	{
		int r = rand();
		int a = (r%(n-1))+1;
		int temp = s;
		int mod = modPow(a, temp, n);
		while(temp!=n-1 && mod!=1 && mod!=n-1)
		{
			mod = (mod*mod)%n;
			temp = 2 * temp;
		}
		if(mod!=n-1 && temp%2==0)
		{
			ans = false;
			break;
		}
	}
	return ans;
}
