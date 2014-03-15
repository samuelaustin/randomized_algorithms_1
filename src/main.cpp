#include <iostream>
#include "aks.cpp"
#include "mr.cpp"
#include "ss.cpp"

using namespace std;
int main(int argc,char* args[])
{	
	for(int i=1; i<100; i++)
	{
		if(aks_p(i))
			cout<<"AKS_P PRIME "<<i<<endl;
		else
			cout<<"AKS_P       "<<i<<endl;
	}
	return 0;
}
