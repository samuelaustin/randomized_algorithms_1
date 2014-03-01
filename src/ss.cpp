#include <sys/time.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;

int mod(long a, long b)
{
   if(b<0)
     return mod(-a,-b);   
   int ret=a%b;
   if(ret<0)
     ret+=b;
   return ret;
}

//a==b(mod n)
bool congruent_modulo(int a,int b,int n)
{
			cout << "ERROR NEGATIVE " << endl;
		cout << "a: " << a << endl;
		cout << "b: " << b << endl;
		cout << "abs(a-b): " << abs(a-b) << endl;
		cout << "n: " << n << endl;
		cout << "result: " << abs(a-b)%n << endl;
	if(abs(a-b)%n==0)
		return true;
	return false;
}


void seed_rand()
{
    struct timeval tv;
    gettimeofday(&tv, NULL);
    srand(tv.tv_sec * tv.tv_usec);
}

int GCD(int a, int b)
{
	if(a==1&&b==0)
		return 1;
	else
	{
		int Intermediate;
		while(b!=0)
		{
			Intermediate=a;
			a=b;
			b=mod(Intermediate,a);
		}
		return a;
	}
	return a;
}


int Jacobi(int a, int n) {
    int ans;

    if (a == 0)
        ans = (n == 1) ? 1 : 0;
    else if (a == 2) {
        switch ( n % 8 ) {
            case 1:
            case 7:
                    ans = 1;
                    break;
            case 3:
            case 5:
                    ans = -1;
                    break;
        }
    }
    else if ( a >= n )
        ans = Jacobi(a%n, n);
    else if ( a % 2 == 0 )
        ans = Jacobi(2,n)*Jacobi(a/2, n);
    else
        ans = ( a % 4 == 3 && n % 4 == 3 ) ? -Jacobi(n,a) : Jacobi(n,a);
    return ans;
}


bool ss(int n, int k)
{
	if(n==2)
		return true;
	if(n%2==0||n<2)
		return false;
	for(int i=0; i<k; i++)
	{
		seed_rand();
		int r = rand()%(n) + 1;
		
		cout << "trace" << endl;
		cout << "power: " << pow(r,(n-1)/2) << endl;
		if( congruent_modulo( Jacobi(r,n), pow(r,(n-1)/2), n) )
			return false;
	}
	return true;
}

int main(int argc, char* args[])
{
	//cout << congruent_modulo(38,14,12) << endl;
	cout << ss(31,31) << endl;
	return 0;
}
