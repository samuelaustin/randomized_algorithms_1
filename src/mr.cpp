#include <iostream>
#include <math.h>
#include <cstdlib>
#include <sys/time.h>
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

void seed_rand()
{
    struct timeval tv;
    gettimeofday(&tv, NULL);
    srand(tv.tv_sec * tv.tv_usec);
}

bool mr_par(int n, int it)
{
	if(n == 2 || n == 3) return true;
	if(n < 2 || (n != 2 && n%2==0)) return false;
	seed_rand();

	int s = n-1;
	while(s%2 == 0)
		s = s/2;
	
	bool ans = true;
	#pragma omp parallel for
	for(int i = 0; i < it; i++)
	{
		#pragma omp flush (ans)
		if(ans)
		{
			int r 		= rand();
			int a 		= (r%(n-1))+1;
			int temp 	= s;
			int mod 	= modPow(a, temp, n);
			while(temp!=n-1 && mod!=1 && mod!=n-1)
			{
				mod	= (mod*mod)%n;
				temp	= 2 * temp;
			}
			if(mod!=n-1 && temp%2==0)
			{
				ans = false;
				#pragma omp flush (ans)
			}
		}
	}
	return ans;
}

bool mr(int n, int it)
{
	if(n == 2 || n == 3) return true;
	if(n < 2 || (n != 2 && n%2==0)) return false;
	
	seed_rand();

	int s = n-1;
	while(s%2 == 0)
		s = s/2;
	
	bool ans = true;
	for(int i = 0; i < it && ans; i++)
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
			ans = false;
	}
	return ans;
}
