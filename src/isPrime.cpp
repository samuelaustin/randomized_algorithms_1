#include <omp.h>
#include <math.h>
#include <iostream>
bool isPrime(unsigned long long n)
{
	if(n == 2 ||  n == 3		) return true;
	if(n  < 2 || (n != 2 && n%2==0)	) return false;
	for(unsigned long long i = 2; i<=sqrt(n); i++)
		if(n%i == 0)
			return false;
	return true;
}

bool isPrime_par(unsigned long long n)
{
	if(n == 2 ||  n == 3		) return true;
	if(n  < 2 || (n != 2 && n%2==0)	) return false;
	unsigned long long sn = ceil(sqrt(n));	
	bool ans = true;
	#pragma omp parallel for
	for(unsigned long long i = 2; i<=sn ; i++)
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
