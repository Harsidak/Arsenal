#include <stdio.h>

int marisa(int n , int w[n+1]) {
    int zero = 0;
    int one = 0;
    int two = 0;
    for (int i=0;i<n;i++) {
        if (w[i]==0) {
            zero++;
        }
        if (w[i]==1) {
            one++;
        }
        if (w[i]==2) {
            two++;
        }
    }

    int min_val = one < two ? one : two;
    int abs_diff = one > two ? (one - two) : (two - one);
    int max_ops = zero + min_val + (abs_diff / 3);
    
    printf("%d\n", max_ops);
    return max_ops;
}


int main() {
    int t;scanf("%d",&t);
    for (int i=0;i<t;i++) {
        int n;scanf("%d",&n);
        int w[n+1];
        for (int j=0;j<n;j++) {
            scanf("%d",&w[j]);
        }
        marisa(n,w);
    }
    return 0;
}