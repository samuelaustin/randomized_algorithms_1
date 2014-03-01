#include <iostream>
#include <cstdlib>
#include <ctime>
#include <math.h>
#include <unistd.h>
#include "aks.cpp"
#include "mr.cpp"
#include <omp.h>
//#include "ss.cpp"

using namespace std;

int main(int argc, char* args[])
{
	//ss(10,3);
	
	//#pragma omp parallel for
	for(int i = 2; i < 5000; i++)
	{
//		bool aks_prime = aks(i);
//		if(aks_prime)
//			cout << "AKS    : " << i << " is a prime" << endl;
//		else
//			cout << "AKS    : " << i << " is not a prime" << endl;

		bool mr_prime = mr_par(i,1000);
		if(mr_prime)
			cout << "MR     : " << i << " is a prime" << endl;
		else
			cout << "MR     : " << i << " is not a prime" << endl;
	}	
	return 0;
	
}
