#include <math.h>
#include <omp.h>
#include "util.cpp"


bool fpt(unsigned long long n, unsigned long long k)
{
	if(n == 2 ||  n == 3		) return true;
	if(n  < 2 || (n != 2 && n%2==0)	) return false;
	seed_rand();

	for(int i=0; i<k; i++)
	{
		unsigned long long a = (rand()%(n-1))+1;
		if(congruent_mod(a,n-1,n)!=1)
			return false;
	}
	return true;
}

bool fpt_p(unsigned long long n, unsigned long long k)
{
	if(n == 2 ||  n == 3		) return true;
	if(n  < 2 || (n != 2 && n%2==0)	) return false;
	seed_rand();
	bool ans = true;
	#pragma omp parallel for
	for(int i=0; i<k; i++)
	{
		#pragma omp flush (ans)
		if(ans)
		{
			unsigned long long a = (rand()%(n-1))+1;
			if(congruent_mod(a,n-1,n)!=1)
			{
				ans=false;
				#pragma omp flush (ans)
			}
		}
	}
	return ans;
}
