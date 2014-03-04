#include <boost/python.hpp>
#include <iostream>
#include <sys/time.h>
#include "aks.cpp"
#include "mr.cpp"
#include "ss.cpp"
#include <omp.h>

using namespace std;
using namespace boost::python;

bool isPrime_py(object n_py)
{
	unsigned long n = extract<unsigned long>(n_py);
	return isPrime(n);
}

bool aks_py(object n_py)
{
	unsigned long n = extract<unsigned long>(n_py);
	return aks(n);
}

bool mr_py(object n_py, object k_py)
{
	unsigned long n = extract<unsigned long>(n_py);
	unsigned long k = extract<unsigned long>(k_py);
	return mr(n,k);
}

bool mr_par_py(object n_py, object k_py)
{
	unsigned long n = extract<unsigned long>(n_py);
	unsigned long k = extract<unsigned long>(k_py);
	return mr_par(n,k);
}

bool ss_py(object n_py, object k_py)
{
	unsigned long n = extract<unsigned long>(n_py);
	unsigned long k = extract<unsigned long>(k_py);
	return ss(n,k);
}

bool ss_par_py(object n_py, object k_py)
{
	unsigned long n = extract<unsigned long>(n_py);
	unsigned long k = extract<unsigned long>(k_py);
	return ss_par(n,k);
}

BOOST_PYTHON_MODULE(prime)
{
	def("isPrime", isPrime_py);
	def("aks", aks_py);
	def("mr", mr_py);
	def("mr_par", mr_par_py);
	def("ss", ss_py);
	def("ss_par", ss_par_py);
}

int main(int argc, char* args[])
{	

	for(int i=1; i<500000; i++)
	{
		if(mr_par(i,25))
			cout<<"MR PRIME "<<i<<endl;
		else
			cout<<"MR       "<<i<<endl;
	}
	
	return 0;
}
