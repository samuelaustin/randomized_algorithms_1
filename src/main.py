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
			datap.append(time_func(50,prime.isPrime,RANGE[i]))
			prange.append(RANGE[i])
		else:
			data.append(time_func(50,prime.isPrime,RANGE[i]))
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
	print("Fermat Primality Test")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.fpt,RANGE[i], k)
	plot.plot(RANGE,data,'.',alpha=0.5,label="Fermat's Primality Test(n," + str(k) + ")")

def test_fpt_par(i, j, k):
	RANGE 	= range(i,j)
	data 	= numpy.zeros(len(RANGE))
	print("Fermat Primality Test Parallel")
	for i in range(0, len(RANGE)):
		data[i]	= time_func(5,prime.fpt_p,RANGE[i], k)
	plot.plot(RANGE,data,'.',alpha=0.5,label="Fermat's Primality Test Parallel(n," + str(k) + ")")

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
	plot.savefig("isPrimev_MR_runtime")
	plot.show()

def compare_isPrime_aks_runtime_complexity():
	_,ax = plot.subplots()
	ax.set_title('Agrawal-Kayal-Saxena (2,6000)' )
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('n')

	#test_isPrime( 2,6000)
	test_aks(2,6000)
	plot.legend()	
	plot.show()
	
	_,ax = plot.subplots()
	ax.set_title('Agrawal-Kayal-Saxena (90000,91000)')
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('n')

	#test_isPrime(90000,90000+6000)
	test_aks(90000,90000+6000)
	plot.legend()
	plot.show()

def compare_isPrime_isPrimep_runtime_complexity():
	_,ax = plot.subplots()
	ax.set_title('Trial Division vs Trial Division Parallel')
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('n')

	test_isPrime_par(2,10000)
	test_isPrime(2,10000)
	plot.legend()
	#plot.savefig("MRP_MR_small_runtime", figsize=(10,16),dpi=100)
	plot.show()

	_,ax = plot.subplots()
	ax.set_title('Trial Division vs Trial Division Parallel')
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('n')

	test_isPrime_par(1000000000,1000000000+10000)
	test_isPrime(1000000000,1000000000+10000)
	plot.legend()
	#plot.savefig("MRP_MR_small_runtime", figsize=(10,16),dpi=100)
	plot.show()

def compare_mr_mrp_runtime_complexity():
	_,ax = plot.subplots()
	ax.set_title('Miller-Rabin vs Miller Rabin Parallel')
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('n')

	test_mr_par(100000+2, 100000+12000, 20)
	test_mr(100000+2, 100000+12000, 20)
	plot.legend()
	#plot.savefig("MRP_MR_small_runtime", figsize=(10,16),dpi=100)
	plot.show()

	_,ax = plot.subplots()
	ax.set_title('Miller-Rabin vs Miller Rabin Parallel')
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('n')
	test_mr_par(100000+2, 100000+12000, 5000)
	test_mr(100000+2, 100000+12000, 5000)
	plot.legend()
	plot.show()

def compare_ss_ssp_runtime_complexity():
	_,ax = plot.subplots()
	ax.set_title('Solovay-Strassen vs Solovay-Strassen Parallel')
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('n')

	test_ss_par(100000+2, 100000+12000, 20)
	test_ss(100000+2, 100000+12000, 20)
	plot.legend()
	plot.show()

	_,ax = plot.subplots()
	ax.set_title('Solovay-Strassen vs Solovay-Strassen Parallel')
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('n')
	test_ss_par(100000+2, 100000+12000, 5000)
	test_ss(100000+2, 100000+12000, 5000)
	plot.legend()
	plot.show()

def compare_fpt_fptp_runtime_complexity():
	_,ax = plot.subplots()
	ax.set_title('Fermat vs Fermat Parallel')
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('n')

	test_fpt_par(100000+2, 100000+12000, 20)
	test_fpt(100000+2, 100000+12000, 20)
	plot.legend()
	plot.show()

	_,ax = plot.subplots()
	ax.set_title('Fermat vs Fermat Parallel')
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('n')
	test_fpt_par(100000+2, 100000+12000, 5000)
	test_fpt(100000+2, 100000+12000, 5000)
	plot.legend()
	plot.show()

def compare_all_runtime_complexity():
	
	_,ax = plot.subplots()
	ax.set_title('Run Time Plot')
	ax.set_ylabel('Run Time')
	ax.set_xlabel('tested number n')

	f = 9999990074039999
	t = f+3*120000
	
	test_mr(f,t, 5)
	test_ss(f,t, 10)
	test_fpt(f,t, 10)
	plot.legend()
	plot.show()


	_,ax = plot.subplots()
	ax.set_title('Run Time Plot')
	ax.set_ylabel('Run Time')
	ax.set_xlabel('tested number n')

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

def fpt_accuracy(i, j, k):
	fpt_errors	= []
	for n in range(i,j):
		ans	= prime.isPrime_par(n)	
		if prime.fpt(n,k) != ans:
			fpt_errors.append(n)
	
	errors = (len(fpt_errors))
	return errors

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
	#print errors
	#print mr_errors	
	#print ss_errors
	#print fpt_errors
	#_,ax = plot.subplots()
	#ax.set_title('Error Histrogram with k=' + str(k))
	#ax.set_ylabel('#errors')
	#ax.set_ylim([0,50])
	#ax.bar(range(0,3), errors, 0.5, color={'r','g','b'})
	#ax.set_xticks(numpy.arange(3)+0.5/2)
	#ax.set_xticklabels(('MR', 'SS', 'FPT'))
	#plot.show() 
	return errors

def compare_accuracy_loop(i,j,k):
	mr_dat = numpy.zeros(k)
	ss_dat = numpy.zeros(k)
	fpt_dat = numpy.zeros(k)
	for r in range(1,k+1):
		(mr,ss,fpt) = compare_accuracy(i,j,r)
		mr_dat[r-1]=mr
		ss_dat[r-1]=ss
		fpt_dat[r-1]=fpt

	_,ax = plot.subplots()
	plot.plot(numpy.array(range(0,k))+1,mr_dat+1,'-r',label="Miller-Rabin")
	plot.plot(numpy.array(range(0,k))+1,ss_dat+1,'-g',label="Solovay-Strassen")
	plot.plot(numpy.array(range(0,k))+1,fpt_dat+1,'-b',label="Fermat's Primality Test")
	
	ax.set_yscale('log')
	#ax.set_xscale('log')
	ax.set_title('Accuracy log log scale, n='+str(j-i))
	ax.set_ylabel('#errors')
	ax.set_xlabel('Itterations k')
	plot.legend()
	plot.show()

	_,ax = plot.subplots()
	ax.set_title('Accuracy, n='+str(j-i))
	ax.set_ylabel('#errors')
	ax.set_xlabel('Itterations k')
	plot.plot(numpy.array(range(0,k))+1,mr_dat,'-r',label="Miller-Rabin")
	plot.plot(numpy.array(range(0,k))+1,ss_dat,'-g',label="Solovay-Strassen")
	plot.plot(numpy.array(range(0,k))+1,fpt_dat,'-b',label="Fermat's Primality Test")
	plot.legend()
	plot.show()
	plot.cla()
	plot.clf()

def compare_accuracy_FPT(i,j,n,k):
	mr_dat_low = numpy.zeros(k)
	ss_dat_low = numpy.zeros(k)
	fpt_dat_low = numpy.zeros(k)
	mr_dat_high = numpy.zeros(k)
	ss_dat_high = numpy.zeros(k)
	fpt_dat_high = numpy.zeros(k)
	for r in range(1,k+1):
		(mr_dat_low[r-1],ss_dat_low[r-1],fpt_dat_low[r-1]) = compare_accuracy(i,i+n,r)
		(mr_dat_high[r-1],ss_dat_high[r-1],fpt_dat_high[r-1]) = compare_accuracy(i,i+n,r)

	_,ax = plot.subplots()
	plot.plot(numpy.array(range(0,k))+1,mr_dat_low+1,'-r',label="Miller-Rabin (low)")
	plot.plot(numpy.array(range(0,k))+1,ss_dat_low+1,'-g',label="Solovay-Strassen (low)")
	plot.plot(numpy.array(range(0,k))+1,fpt_dat_low+1,'-b',label="Fermat's Primality Test (low)")

	plot.plot(numpy.array(range(0,k))+1,mr_dat_high+1,'--r',label="Miller-Rabin (high)")
	plot.plot(numpy.array(range(0,k))+1,ss_dat_high+1,'--g',label="Solovay-Strassen (high)")
	plot.plot(numpy.array(range(0,k))+1,fpt_dat_high+1,'--b',label="Fermat's Primality Test (high)")

	
	ax.set_yscale('log')
	ax.set_xscale('log')
	ax.set_title('Accuracy log log scale, n='+str(j-i))
	ax.set_ylabel('#errors')
	ax.set_xlabel('Itterations k')
	plot.legend()
	plot.show()

	plot.cla()
	plot.clf()
	_,ax = plot.subplots()
	ax.set_title('Accuracy, n='+str(j-i))
	ax.set_ylabel('#errors')
	ax.set_xlabel('Itterations k')
	plot.plot(numpy.array(range(0,k))+1,mr_dat_low+1,'-r',label="Miller-Rabin (low)")
	plot.plot(numpy.array(range(0,k))+1,ss_dat_low+1,'-g',label="Solovay-Strassen (low)")
	plot.plot(numpy.array(range(0,k))+1,fpt_dat_low+1,'-b',label="Fermat's Primality Test (low)")

	plot.plot(numpy.array(range(0,k))+1,mr_dat_high+1,'--r',label="Miller-Rabin (high)")
	plot.plot(numpy.array(range(0,k))+1,ss_dat_high+1,'--g',label="Solovay-Strassen (high)")
	plot.plot(numpy.array(range(0,k))+1,fpt_dat_high+1,'--b',label="Fermat's Primality Test (high)")
	plot.legend()
	plot.show()

def compare_isPrime_Randomized(i,j,k):
	_,ax = plot.subplots()
	ax.set_title('Trial Division and Randomized run times')
	ax.set_ylabel('Run Time (us)')
	ax.set_xlabel('Number n')

	test_mr(i,j,k)
	test_ss(i,j,k)
	test_fpt(i,j,k)
	test_isPrime(i,j)

	plot.legend()
	plot.show()
		

#compare_isPrime_isPrimep_runtime_complexity()
#compare_mr_mrp_runtime_complexity()
#compare_ss_ssp_runtime_complexity()
#compare_fpt_fptp_runtime_complexity()

#compare_all_runtime_complexity()
#compare_all_parallel_runtime_complexity()

#visualize_isPrime(2, 3*10**6)
#compare_isPrime_aks_runtime_complexity()

#compare_accuracy(2,500000,1)
#compare_accuracy(2,500000,2)
#compare_accuracy(2,500000,3)
#compare_accuracy(2,500000,4)

#compare_accuracy_FPT(1,200000,200000,25)

compare_isPrime_Randomized(1000000000,1000010000,10)


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
