#include <stdio.h>

long long int min_value(long long int x, long long int y) {
    return (x < y) ? x : y;
}

long long int calc(long long int n ,long long int a,long long int b) {
    long long int totali = 0;
    if (3*a <= b) {
        totali = a*n;
    }
    else {
        int group = n/3;
        int left = n%3;

        totali = group*b;
        if (left == 1) {
            totali += min_value(a,b);
        }
        if (left == 2) {
            totali += min_value(2*a,b);
        }
    }
    printf("%lld\n",totali);
}


int main() {
    int t; scanf("%d",&t);for (int ik = 0; ik<t;++ik) {
       long long int n,a,b;
        scanf("%lld %lld %lld",&n,&a,&b);
        calc(n,a,b);
    }
    return 0;
}