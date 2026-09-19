#include <stdio.h>
#include <math.h>

int rem(int n, int x1, int x2, int k) {
    int one = abs(x1 - x2);
    int two = n - abs(x1 - x2);
    int d = 0;if (one <= two){d = one;}if (two<one){d = two;}

    int time = 0;
    if (n<=3) {
        time = d;
    }if (n>=4) {
        if (n%2==0){
            time = d+k;
        }else {
            time = d+k;
        }
    }

    printf("%d\n", time);
    return time;
}
int main() {
    int t; scanf("%d",&t);
    for (int i = 0; i < t; i++) {
        int n,x1,x2, k;scanf("%d %d %d %d",&n,&x1,&x2,&k);
        rem(n,x1,x2,k);
    }
    return 0;
}