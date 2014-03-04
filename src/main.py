import matplotlib.pyplot as plot
import numpy
import prime
import timeit

def time_func(it,func,*args):
	t=timeit.Timer(lambda: func(*args))
	return t.timeit(number=it)/it
	return data 

def test_isPrime(i, j):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("isPrime")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.isPrime,RANGE[i])
	plot.plot(RANGE,data,'+',label="isPrime(n)")
	return data 

def test_aks(i, j):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("aks")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.aks,RANGE[i])
	plot.plot(RANGE,data,'+',label="aks(n)")
	return data 

def test_ss(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("ss")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.ss,RANGE[i], k)
	plot.plot(RANGE,data,'+',label="ss(n," + str(k) + ")")
	return data 

def test_ss_par(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("ss_par")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.ss_par,RANGE[i], k)
	plot.plot(RANGE,data,'+',label="ss_par(n," + str(k) + ")")
	return data 

def test_mr(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("mr")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.mr,RANGE[i], k)
	plot.plot(RANGE,data,'+',label="mr(n," + str(k) + ")")
	return data 

def test_mr_par(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("mr_par")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.mr_par,RANGE[i], k)
	plot.plot(RANGE,data,'+',label="mr_par(n," + str(k) + ")")
	return data 

test_isPrime(2,1000)
test_aks(2,1000)
plot.legend()	
plot.show()

test_mr(100000+2, 100000+60000, 50)
test_mr_par(100000+2, 100000+60000, 50)
plot.legend()	
plot.show()

test_ss(100000+2, 100000+60000, 50)
test_ss_par(100000+2, 100000+60000, 50)
plot.legend()	
plot.show()

test_mr(100000+2, 100000+60000, 30)
test_mr_par(100000+2, 100000+60000, 30)
test_ss(100000+2, 100000+60000, 30)
test_ss_par(100000+2, 100000+60000, 30)
plot.legend()	
plot.show()
