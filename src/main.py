import matplotlib.pyplot as plot
import numpy
import prime
import timeit

def time_func(it,func,*args):
	t=timeit.Timer(lambda: func(*args))
	return t.timeit(number=it)/it

def test_isPrime(i, j):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("isPrime")
	for i in range(0, len(RANGE)):
		data[i]		= time_func(5,prime.isPrime,RANGE[i])
	plot.plot(RANGE,data,label="isPrime(n)")
	plot.legend()	
	plot.show()

def test_aks(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("aks")
	for i in range(0, len(RANGE)):
		data[i]		= time_func(5,prime.aks,RANGE[i])
	plot.plot(RANGE,data,label="aks(n)")
	plot.legend()	
	plot.show()

def test_ss(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("ss")
	for i in range(0, len(RANGE)):
		data[i]		= time_func(5,prime.ss,RANGE[i], k)
	plot.plot(RANGE,data,label="ss(n," + str(k) + ")")
	plot.legend()	
	plot.show()

def test_ss_par(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("ss_par")
	for i in range(0, len(RANGE)):
		data[i]		= time_func(5,prime.ss_par,RANGE[i], k)
	plot.plot(RANGE,data,label="isPrime(n," + str(k) + ")")
	plot.legend()	
	plot.show()

def test_mr(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("mr")
	for i in range(0, len(RANGE)):
		data[i]		= time_func(5,prime.mr,RANGE[i], k)
	plot.plot(RANGE,data,label="isPrime(n," + str(k) + ")")
	plot.legend()	
	plot.show()

def test_mr_par(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("mr_par")
	for i in range(0, len(RANGE)):
		data[i]		= time_func(5,prime.mr_par,RANGE[i], k)
	plot.plot(RANGE,data,label="isPrime(n," + str(k) + ")")
	plot.legend()	
	plot.show()


i = 2
j = 60000
k = 25

test_ss_par(i, j, k)

