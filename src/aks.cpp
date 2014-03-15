#include "util.cpp"
#include "NTL/ZZ.h"
#include "NTL/ZZ_pX.h"
#include <gmp.h>
#include <gmpxx.h>

using namespace std;
using namespace NTL;


//Dit algorithme presteerd nog steeds slechter dan isPrime.
bool aks(unsigned long n)
{
	if(n  < 2 || (n != 2 && n%2==0)	) return false;

	//1
	for(int a = 2; pow(a, 2) <= n; a++)
	{
		double b = log(n)/log(a);
		if(b==(int)b && b>1)
			return false;
	}
	//2
	float t = pow(log2((float)n),2);
	unsigned long r;
	for(r=2;r<n;r++)
		if(mo(r,n)>t)
			break;

	//3
	for(unsigned int a = 0; a <= r; a++)
		if(1 < gcd(a,n) && gcd(a,n) < n)
			return false;
	//4
	if(n <= r)
	{
		return true;
	}
	//5
	ZZ_p::init(to_ZZ(n));
	ZZ_pX f(r, 1); 
	f -= 1;
	const ZZ_pXModulus pf(f);
	ZZ_pX rPoly(1, 1);		// x
	PowerMod(rPoly, rPoly, n, pf);	// x^n

	unsigned int a;
	for(int a = 1; a <= 2*sqrt((float)r)*log2((float)n); a++)
	{
		ZZ_pX lPoly(1, 1);		// x		
		lPoly -= a;			// x - a
		PowerMod(lPoly, lPoly, n, pf);	// (x - a)^n
		lPoly += a;			// (x - a)^n + a
		if (lPoly != rPoly)
			return false;
		
	}
	return true;
}


bool aks_p(unsigned long n)
{
	if(n  < 2 || (n != 2 && n%2==0)	) return false;

	bool isPrime = true;

	//1
	unsigned long long root = sqrt(n);
	#pragma omp parallel for	
	for(int a = 2; a <= root; a++)
	{
		#pragma omp flush (isPrime)
		if(isPrime)
		{
			double b = log(n)/log(a);
			if(b==(int)b && b>1) 
			{
				isPrime = false;
				#pragma omp flush (isPrime)
			}
		}
	}
	if(!isPrime) return false;

	//2
	float t = pow(log2((float)n),2);
	unsigned long r;
	for(r=2;r<n;r++)
		if(mo(r,n)>t)
			break;

	//3
	#pragma omp parallel for
	for(unsigned int a = 0; a <= r; a++)
	{
		#pragma omp flush (isPrime)
		if(isPrime)
		{
			if(1 < gcd(a,n) && gcd(a,n) < n) 
			{
				isPrime = false;
				#pragma omp flush (isPrime)
			}
		}
	}
	if(!isPrime) return false;

	//4
	if(n <= r)
	{
		return true;
	}

	//5
	ZZ_p::init(to_ZZ(n));
	ZZ_pX f(r, 1); 
	f -= 1;
	const ZZ_pXModulus pf(f);
	ZZ_pX rPoly(1, 1);				// x
	PowerMod(rPoly, rPoly, n, pf);	// x^n

	unsigned int a;
	unsigned long long bound = 2*sqrt((float)r)*log2((float)n);
	for(int a = 1; a <= bound; a++)
	{
		ZZ_pX lPoly(1, 1);				// x		
		lPoly -= a;						// x - a
		PowerMod(lPoly, lPoly, n, pf);	// (x - a)^n
		lPoly += a;						// (x - a)^n + a
		if (lPoly != rPoly)
			return false;
		
	}
	return true;
}
