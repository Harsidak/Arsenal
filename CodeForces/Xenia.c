#include <stdio.h>

int main(){

    long long n,m;
    scanf("%lld %lld",&n,&m);

    long long current = 1;
    long long time = 0;

    for(int i=0;i<m;i++){

        long long target;
        scanf("%lld",&target);

        if(target >= current)
            time += target - current;
        else
            time += (n - current) + target;

        current = target;
    }

    printf("%lld",time);

    return 0;
}