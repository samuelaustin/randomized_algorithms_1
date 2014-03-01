#include <iostream>
#include <math.h>
#include <unistd.h>
#include "aks.cpp"
#include "mr.cpp"

using namespace std;

int main(int argc, char* args[])
{
	for(int i = 2; i < 200; i++)
	{
		bool aks_prime = aks(i);
		if(aks_prime)
			cout << "AKS    : " << i << " is a prime" << endl;
		else
			cout << "AKS    : " << i << " is not a prime" << endl;

		bool mr_prime = mr(i, 1);
		if(mr_prime)
			cout << "MR     : " << i << " is a prime" << endl;
		else
			cout << "MR     : " << i << " is not a prime" << endl;

		//usleep(1000000);
		//bool is_prime = IsPrime(i);
		
		//if(is_prime)
		//	cout << "isPrime: " << i << " is a prime" << endl;
		//else
		//	cout << "isPrime: " << i << " is not a prime" << endl;
	}	
	return 0;
}
