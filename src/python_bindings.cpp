#include <boost/python.hpp>
#include "util.cpp"
#include "aks.cpp"
#include "mr.cpp"
#include "ss.cpp"
#include "fpt.cpp"

using namespace boost::python;

BOOST_PYTHON_MODULE(prime)
{
	def("isPrime", isPrime);
	def("isPrime_par", isPrime_par);
	def("aks", aks);
	def("fpt", fpt);
	def("fpt_p", fpt_p);
	def("mr", mr);
	def("mr_par", mr_par);
	def("ss", ss);
	def("ss_par", ss_par);
}
