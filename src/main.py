import matplotlib.pyplot as plot
import numpy
import prime
import timeit

def time_func(it,func,*args):
	t=timeit.Timer(lambda: func(*args))
	return t.timeit(number=it)/it*1000000

def visualize_isPrime(i, j):
	RANGE 	= range(i,j)
	data 	= []
	crange	= []
	datap 	= []
	prange  = []
	print("isPrime")
	for i in range(0, len(RANGE)):
		if prime.isPrime(RANGE[i]):
			datap.append(time_func(5,prime.isPrime,RANGE[i]))
			prange.append(RANGE[i])
		else:
			data.append(time_func(5,prime.isPrime,RANGE[i]))
			crange.append(RANGE[i])
	_,ax = plot.subplots()
	ax.set_title('Trial Division Run Time')
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('Number n')
	plot.plot(crange,data,'.',color="b",alpha=0.5,label="Trial Division is Composite")
	plot.plot(prange,datap,'.',color="r",alpha=0.5,label="Trial Division is Prime")
	plot.legend()
	plot.show()

def test_isPrime(i, j):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("Trial Division")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.isPrime,RANGE[i])
	plot.plot(RANGE,data,'.',alpha=0.5,label="Trial Division(n)")

def test_isPrime_par(i, j):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("Trial Division Parallel")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.isPrime_par,RANGE[i])
	plot.plot(RANGE,data,'.',alpha=0.5,label="Trial Division Parallel(n)")

def test_aks(i, j):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("Agrawal-Kayal-Saxena")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.aks,RANGE[i])
	plot.plot(RANGE,data,'.',alpha=0.5,label="Agrawal-Kayal-Saxena(n)")
	return data 

def test_ss(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("Solovay-Strassen")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.ss,RANGE[i], k)
	plot.plot(RANGE,data,'.',alpha=0.5,label="Solovay-Strassen(n," + str(k) + ")")

def test_ss_par(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("Solovay-Strassen Parallel")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.ss_par,RANGE[i], k)
	plot.plot(RANGE,data,'.',alpha=0.5,label="Solovay-Strassen Parallel(n," + str(k) + ")")

def test_mr(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("Miller-Rabin")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.mr,RANGE[i], k)
	plot.plot(RANGE,data,'.',alpha=0.5,label="Miller-Rabin(n," + str(k) + ")")

def test_mr_par(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("Miller-Rabin Parallel")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.mr_par,RANGE[i], k)
	plot.plot(RANGE,data,'.',alpha=0.5,label="Miller-Rabin Parallel(n," + str(k) + ")")

def test_fpt(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("Fourrier Primality Test")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.fpt,RANGE[i], k)
	plot.plot(RANGE,data,'.',alpha=0.5,label="Fourrier Primality Test(n," + str(k) + ")")

def test_fpt_p(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("Fourrier Primality Test Parallel")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.fpt_p,RANGE[i], k)
	plot.plot(RANGE,data,'.',alpha=0.5,label="Fourrier Primality Test Parallel(n," + str(k) + ")")

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
	test_isPrime( 2,6000)
	test_aks(2,6000)
	plot.legend()	
	plot.show()
	
	test_isPrime(900000,900000+1000)
	test_aks(900000,900000+1000)
	plot.legend()	
	plot.show()

def compare_mr_mrp_runtime_complexity():
	_,ax = plot.subplots()
	ax.set_title('Miller-Rabin vs Miller Rabin Parallel')
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('n')

	test_mr_par(100000+2, 100000+12000, 20)
	test_mr(100000+2, 100000+12000, 20)
	plot.legend()
	plot.show()

	test_mr_par(100000+2, 100000+12000, 5000)
	test_mr(100000+2, 100000+12000, 5000)
	plot.legend()
	plot.show()

def compare_all_runtime_complexity():
	
	_,ax = plot.subplots()
	ax.set_title('Run Time Plot')
	ax.set_ylabel('Run Time')
	ax.set_xlabel('tested number n')

	f = 9999990074039999
	t = f+3*120000
	test_mr(f,t, 50)
	test_ss(f,t, 100)
	test_fpt(f,t, 100)
	plot.legend()
	plot.show()

def compare_all_parallel_runtime_complexity():
	
	_,ax = plot.subplots()
	ax.set_title('Run Time Plot')
	ax.set_ylabel('Run Time')
	ax.set_xlabel('tested number n')

	f = 9999990074039999
	t = f+3*12000
	test_mr_par(f,t,250)
	test_ss_par(f,t,500)
	test_fpt_p(f,t,500)
	plot.legend()
	plot.show()

def compare_accuracy(i, j, k):
	mr_errors	= []
	ss_errors	= []
	fpt_errors	= []
	for n in range(i,j):
		ans	= prime.isPrime_par(n)	
		if  prime.mr(n,k) != ans:		
			mr_errors.append(n)
		if prime.ss(n,k) != ans:
			ss_errors.append(n)
		if prime.fpt(n,k) != ans:
			fpt_errors.append(n)
	
	errors = (len(mr_errors), len(ss_errors), len(fpt_errors))
	print errors
	print mr_errors	
	print ss_errors
	print fpt_errors
	_,ax = plot.subplots()
	ax.set_title('Error Histrogram with k=' + str(k))
	ax.set_ylabel('#errors')
	ax.bar(range(0,3), errors, 0.5, color={'r','g','b'})
	ax.set_xticks(numpy.arange(3)+0.5/2)
	ax.set_xticklabels(('MR', 'SS', 'FPT'))
	plot.show() 


compare_all_parallel_runtime_complexity()
#compare_mr_mrp_runtime_complexity()
#visualize_isPrime(2, 3*10**6)
#compare_isPrime_aks_runtime_complexity()
#compare_accuracy(2,500000,1)
#compare_all_runtime_complexity()




#for i in range(2,35):
#	print(str(i) + ": " + str(prime.fpt(i,50)))


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
