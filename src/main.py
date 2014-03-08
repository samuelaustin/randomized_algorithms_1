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

def test_isPrime_par(i, j):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("isPrime_par")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.isPrime_par,RANGE[i])
	plot.plot(RANGE,data,'+',label="isPrime_par(n)")
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

def test_fpt(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("fpt")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.fpt,RANGE[i], k)
	plot.plot(RANGE,data,'+',label="fpt(n," + str(k) + ")")
	return data 

def test_fpt_p(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("fpt_p")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.fpt_p,RANGE[i], k)
	plot.plot(RANGE,data,'+',label="fpt_p(n," + str(k) + ")")
	return data 

def compare_isPrime_mr_runtime_complexity():
	#Small numbers
	test_mr(1000+2, 1000+60000, 25)
	test_isPrime(1000+2, 1000+60000)
	plot.legend()	
	plot.show()

	#Large numbers
	test_mr(515396078+2, 515396078+60000, 25)
	test_isPrime(515396078+2, 515396078+60000)
	plot.legend()	
	plot.show()

def compare_isPrime_aks_runtime_complexity():
	test_isPrime( 2,3000)
	test_aks(2,3000)
	plot.legend()	
	plot.show()
	
	test_isPrime(900000,900000+1000)
	test_aks(900000,900000+1000)
	plot.legend()	
	plot.show()

def compare_mr_mrp_runtime_complexity():
	test_mr_par(100000+2, 100000+60000, 50)
	test_mr(100000+2, 100000+60000, 50)
	plot.legend()	
	plot.show()

def compare_all_runtime_complexity():
	f = 29999990074039999
	t = f+120000
	test_mr_par(f,t,25)
	test_mr(f,t, 25)
	test_ss_par(f,t,50)
	test_ss(f,t, 50)
	test_fpt_p(f,t,50)
	test_fpt(f,t, 50)
	plot.legend()	
	plot.show()

for i in range(2,35):
	print(str(i) + ": " + str(prime.fpt(i,50)))
compare_all_runtime_complexity()

#test_ss(100000+2, 100000+60000, 50)
#test_ss_par(100000+2, 100000+60000, 50)
#plot.legend()	
#plot.show()

#test_mr(100000+2, 100000+60000, 50)
#test_mr_par(100000+2, 100000+60000, 50)
#test_ss(100000+2, 100000+60000, 50)
#test_ss_par(100000+2, 100000+60000, 50)
#plot.legend()	
#plot.show()
