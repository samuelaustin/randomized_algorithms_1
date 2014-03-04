#include <iostream>

#include "aks.cpp"
#include "mr.cpp"
#include "ss.cpp"

using namespace std;

int main(int argc, char* args[])
{	
	for(int i=2; i<0; i++)
	{
		if(aks(i))
			cout<<"AKS PRIME "<<i<<endl;
		else
			cout<<"AKS       "<<i<<endl;
	}
	for(int i=2; i<0; i++)
	{
		if(mr(i,1000))
			cout<<"MR PRIME "<<i<<endl;
		else
			cout<<"MR       "<<i<<endl;
	}
	for(int i=2; i<0; i++)
	{
		if(mr_par(i,1000))
			cout<<"MR PARALLEL PRIME "<<i<<endl;
		else
			cout<<"MR PARALLEL       "<<i<<endl;
	}
	for(int i=2; i<0; i++)
	{
		if(ss(i,1000))
			cout<<"SS PRIME "<<i<<endl;
		else
			cout<<"SS       "<<i<<endl;
	}
	for(int i=2; i<100000; i++)
	{
		if(ss_par(i,4000))
			cout<<"SS PARALLEL PRIME "<<i<<endl;
		else
			cout<<"SS PARALLEL       "<<i<<endl;
	}
	return 0;
}
