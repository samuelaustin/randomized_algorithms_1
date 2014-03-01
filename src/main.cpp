#include <iostream>
#include <math.h>
#include "util.cpp"
#include "NTL/ZZ.h"
#include "NTL/ZZ_pX.h"

using namespace std;
using namespace NTL;

bool aks(int n)
{
	//1
	for(int a = 2; pow(a, 2) <= n; a++)
	{
		int prod;
		int b = 2;
		do {
			prod = pow(a,b);
			if(prod==n)
				return false;
			b++;
		} while(prod<=n);
	}
	//2
	float t = pow(log2((float)n),2);
	int r;
	for(r=2;r<n;r++)
		if(mo(r,n)>t)
		{
			break;
		}
	//3
	for(int a = 0; 1 < gcd(a,n) && gcd(a,n) < n; a++)
		if(a<=r)
	//4		return false;
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
		{
			return false;
		}
	}
	return true;
}

int main(int argc, char* args[])
{
	for(int i = 2; i < 200; i++)
	{
		bool aks_prime = aks(i);
		if(isPrime)
			cout << "AKS: " << i << " is a prime" << endl;
		else
			cout << "AKS: " << i << " is not a prime" << endl;

		bool is_prime = isPrime(i);
		if(is_prime)
			cout << "isPrime: " << i << " is a prime" << endl;
		else
			cout << "isPrime: " << i << " is not a prime" << endl;
	}	
	return 0;
}
