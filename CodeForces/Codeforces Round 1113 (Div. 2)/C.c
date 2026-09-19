#include <stdio.h>
#include <stdlib.h>

long long a[2 * 200005];
int lp[200005];
long long dp[2 * 200005 + 5];

long long mux(long long x, long long y) {
    return (x > y) ? x : y;
}

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        int n;
        scanf("%d", &n);
        int tll = 2 * n;
        for (int i = 1; i <= n; i++) {
            lp[i] = 0;
        }

        for (int i = 1; i <= tll; i++) {
            scanf("%lld", &a[i]);
            lp[a[i]] = i; 
        }

        dp[tll + 1] = 0;

        for (int i = tll; i >= 1; i--) {
            dp[i] = 1 + dp[i + 1];

            int j = lp[a[i]];
            if (j >= i) {
                long long len = j - i + 1;
                long long block_score = len * len + dp[j + 1];
                dp[i] = mux(dp[i], block_score);
            }
        }

        printf("%lld\n", dp[1]);
    }
    return 0;
}