#include <cstring>
#include <iostream>
#include <cstdlib>

using namespace std;

int modulo(int base, int exponent, int mod)
{
	int x = 1;
	int y = base;
	while (exponent > 0)
	{
		if (exponent % 2 == 1)
			x = (x * y) % mod;

		y = (y * y) % mod;
		exponent = exponent / 2;
	}
	return x % mod;
}

int jacobi(int a,int n)
{
	if (!a) 
		return 0;

	int ans = 1;
	int temp;

	if (a < 0)
	{
		a = -a;
		if (n % 4 == 3) 
			ans=-ans; 
	}

	if (a == 1) 
		return ans;

	while (a)
	{
		if (a < 0)
		{
			a = -a;
			if (n % 4 == 3) 
				ans = -ans;  
		}
		while (a % 2 == 0)
		{
			a = a / 2;
			if (n % 8 == 3 || n % 8 == 5) 
				ans = -ans;    
		}
		swap(a, n);

		if (a % 4 == 3 && n % 4 == 3) 
			ans = -ans;

		a = a % n;
		if (a > n / 2) 
			a = a - n; 
	}

	if (n == 1) 
		return ans;
	return 0; 
}

bool ss(int n, int k)
{
	if (n < 2) 
		return false;

	if (n != 2 && n % 2 == 0) 
		return false;
	seed_rand();
	for (int i = 0; i < k; i++)
	{
		int a = rand() % (n - 1) + 1;
		int jacobian = (n + jacobi(a, n)) % n;
		int mod = modulo(a, (n - 1) / 2, n);

		if (!jacobian || mod != jacobian)
			return false;
	}
	return true;
}

bool ss_par(int n, int k)
{
	if (n < 2) 
		return false;

	if (n != 2 && n % 2 == 0) 
		return false;
	seed_rand();

	bool ans = true;
	#pragma omp parallel for
	for (int i = 0; i < k; i++)
	{
		#pragma omp flush (ans)
		if(ans)
		{
			int a = rand() % (n - 1) + 1;
			int jacobian = (n + jacobi(a, n)) % n;
			int mod = modulo(a, (n - 1) / 2, n);

			if (!jacobian || mod != jacobian)
			{
				ans = false;
				#pragma omp flush (ans)
			}
		}
	}
	return ans;
}
