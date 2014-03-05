#include <iostream>
#include "aks.cpp"
#include "mr.cpp"
#include "ss.cpp"

using namespace std;
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
