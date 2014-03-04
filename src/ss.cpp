#include "util.cpp"

using namespace std;

bool ss(unsigned long n, unsigned int k)
{
	if (n < 2) 
		return false;

	if (n != 2 && n%2 == 0) 
		return false;
	seed_rand();
	for(unsigned int i = 0; i < k; i++)
	{
		unsigned long a = rand()%(n-1)+1;
		unsigned long jacobian = (n+jacobi(a,n))%n;
		unsigned long mod = congruent_mod(a,(n-1)/2,n);

		if (!jacobian || mod != jacobian)
			return false;
	}
	return true;
}

bool ss_par(unsigned long n, int k)
{
	if (n<2) 
		return false;

	if (n!=2 && n%2 == 0) 
		return false;
	seed_rand();

	bool ans = true;
	#pragma omp parallel for
	for(unsigned int i = 0; i<k; i++)
	{
		#pragma omp flush (ans)
		if(ans)
		{
			unsigned long a = rand()%(n-1)+1;
			unsigned long jacobian = (n+jacobi(a, n))%n;
			unsigned long mod = congruent_mod(a,(n-1)/2,n);

			if (!jacobian || mod != jacobian)
			{
				ans = false;
				#pragma omp flush (ans)
			}
		}
	}
	return ans;
}
