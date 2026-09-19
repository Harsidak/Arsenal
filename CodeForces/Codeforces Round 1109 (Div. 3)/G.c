#include <stdio.h>
#include <stdlib.h>

#define MAXIMUM 200005


long long tree[MAXIMUM];
long long a[MAXIMUM];
long long dp[MAXIMUM];
int bong[MAXIMUM], nxt[MAXIMUM];
int n;

int lowbit(int x) {return x & (-x);}

void update(int ps, long long val){
    while (ps <= n){
        if (val > tree[ps]) tree[ps] = val;
        ps += lowbit(ps);
    }
}

long long query(int ps){
    long long rest_ofit = 0;
    while(ps > 0){
        if(tree[ps] > rest_ofit) rest_ofit = tree[ps];
        ps -= lowbit(ps);
    }
    return rest_ofit;
}


int main(){
    int tests; scanf("%d",&tests);

    while(tests--){
        scanf("%d",&n);

        for(int i = 0;i < n;i++){scanf("%lld",&a[i]);}
        for (int i = 1;i <= n; i++) tree[i] = 0;
        for(int i = 0; i < n; i++) bong[i] = -1;

        for(int j = 0; j < n; j++){
            long long t = (long long)j + a[j] + 1;
            if(t < n){ nxt[j] = bong[t]; bong[t] = j; }
        }
        long long answer = 0;
        for(int i = 0;i < n;i++){
            for(int j = bong[i];j != -1;j = nxt[j]){
                update(j+1, dp[j]);
            }
            long long lim = i - a[i];
            long long best = 0;
            if (lim > 0) best = query((int)lim);


            dp[i] = a[i] + best;
            if (dp[i] > answer) answer = dp[i];
        }
        printf("%lld\n", answer);
    }
    return 0;
}