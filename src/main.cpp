#include <boost/python.hpp>
#include <iostream>
#include "aks.cpp"
#include "mr.cpp"
#include "ss.cpp"

using namespace std;
using namespace boost::python;

BOOST_PYTHON_MODULE(prime)
{
	def("isPrime",isPrime);
	def("aks",aks);
	def("mr",mr);
	def("mr_par",mr_par);
	def("ss",ss);
	def("ss_par",ss_par);
}

int main(int argc,char* args[])
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
