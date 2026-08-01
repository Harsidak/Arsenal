#include <stdio.h>
#include <stdlib.h>

long long Bs(long long x, long long p[], long long B[], int m){
    int low = 1;
    int high = m;
    long long ans = 0;

    while(low <= high){
        int mid = low + (high - low) / 2;
        if(p[mid] <= x){
            ans = mid;
            low = mid + 1;
        }else {
            high = mid - 1;
        }
    }

        return (long long)B[ans];
}
int main(){
    int t;scanf("%d",&t);
    while(t--){
        long long n, d; int m; scanf("%lld %d %lld", &n, &m, &d);

        long long p[m+1];
        long long r[m+1];  
        for(int i = 1; i <= m; i++){
            scanf("%lld %lld", &p[i], &r[i]);
        }

        long long B[m+1];
        B[0] = 0;
        for(int i = 1; i <= m; i++){
            B[i] = B[i-1] + r[i];
        }
        long long S = B[m];

        int fou = 0;
        for(int i = 1; i <= m && !fou; i++){
            for(int j = i; j <= m && !fou; j++){
                long long t = p[i] + p[j] + 1;
                long long val = B[i] + B[j];
                if(t < n){
                    if(val - Bs(t, p, B, m) > d) fou = 1;
                } else {
                    if(val - S - Bs(t - n, p, B, m) > d) fou = 1;
                }
            }
        }

        if(fou == 1){
            printf("YES\n");
        }else{
            printf("NO\n");
        }
    }
    return 0;
}