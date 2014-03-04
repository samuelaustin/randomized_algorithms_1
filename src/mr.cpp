#include <omp.h>
#include "util.cpp"
#include <iostream>
using namespace std;

bool mr_par(unsigned long n, unsigned int it)
{
	if(n == 2 ||  n == 3		) return true;
	if(n  < 2 || (n != 2 && n%2==0)	) return false;
	seed_rand();

	unsigned long s = n-1;
	while(s%2 == 0)
		s = s/2;
	
	bool ans = true;
	#pragma omp parallel for
	for(unsigned int i = 0; i < it; i++)
	{
		#pragma omp flush (ans)
		if(ans)
		{
			unsigned long r 	= rand();
			unsigned long a 	= (r%(n-1))+1;
			unsigned long temp 	= s;
			unsigned long mod 	= congruent_mod(a,temp,n);
			
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

bool mr(unsigned long n, unsigned int it)
{
	if(n == 2 ||  n == 3		) return true;
	if(n  < 2 || (n != 2 && n%2==0)	) return false;
	seed_rand();

	unsigned long s = n-1;
	while(s%2 == 0)
		s = s/2;
	
	bool ans = true;
	for(unsigned int i = 0; i < it ; i++)
	{
		unsigned long r = rand();
		unsigned long a = (r%(n-1))+1;
		unsigned long temp = s;
		unsigned long mod = congruent_mod(a, temp, n);
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
