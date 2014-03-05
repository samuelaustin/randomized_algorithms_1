python:
	g++ -shared -o prime.so python_bindings.cpp -lntl -fopenmp -lgmpxx -lgmp -O3 -std=c++11 -lboost_python -lboost_system -lpython2.7 -I/usr/include/python2.7 -fPIC
main:
	g++ main.cpp -o prime -lntl -fopenmp -lgmpxx -lgmp -O3 -std=c++11 -lboost_python -lboost_system -lpython2.7 -I/usr/include/python2.7 -fPIC
