#include<iostream>
using namespace std;

int main()
{
    int cash[8];
    cash[0] = 2000;
    cash[1] = 1000;
    cash[2] = 500;
    cash[3] = 100;
    cash[4] = 50;
    cash[5] = 10;
    cash[6] = 5;
    cash[7] = 1;

    int n, i;

    while( cin >> n )
    {
        cout << n << "=";
        for( i = 0 ; i <= 7 ; i++ )
        {
            if( n >= cash[i] )
            {
                cout << cash[i] << "*" << n/cash[i] << " ";
                n = n%cash[i];
            }
        }
        cout << endl;
    }
    return 0;
}