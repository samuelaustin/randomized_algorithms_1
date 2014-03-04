#include <omp.h>
#include <math.h>
#include <iostream>
bool isPrime(unsigned long n)
{
	for(unsigned long i = 2; i < n; i++)
		if(n%i == 0)
			return false;
	return true;
}

bool isPrime_par(unsigned long n)
{
	bool ans = true;
	#pragma omp parallel for
	for(unsigned long i = 2; i<n ; i++)
	{
		#pragma omp flush (ans)
		if(ans)
			if(n%i == 0)
			{
				ans=false;
				#pragma omp flush (ans)
			}				
	}
	return ans;
}
