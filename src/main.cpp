#include <iostream>

#include "aks.cpp"
#include "mr.cpp"

using namespace std;

int main(int argc, char* args[])
{	
	for(int i=2; i<1000; i++)
	{
		if(aks(i))
			cout<<"AKS PRIME "<<i<<endl;
		else
			cout<<"AKS       "<<i<<endl;
	}
	for(int i=2; i<10; i++)
	{
		if(mr(i,100))
			cout<<"MR PRIME "<<i<<endl;
		else
			cout<<"MR       "<<i<<endl;
	}
	for(int i=2; i<60000; i++)
	{
		if(mr_par(i,200))
			cout<<"MR PARALLEL PRIME "<<i<<endl;
		else
			cout<<"MR PARALLEL       "<<i<<endl;
	}
	return 0;
}
