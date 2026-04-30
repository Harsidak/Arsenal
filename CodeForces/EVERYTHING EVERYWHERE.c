#include <stdio.h>

static long long gcd(long long a, long long b) {
    while (b) { a %= b; long long t = a; a = b; b = t; }
    return a;
}

int main(void) {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        int p[200005];
        for (int i = 0; i < n; i++)
            scanf("%d", &p[i]);

        long long ans = 0;
        for (int i = 0; i < n - 1; i++) {
            long long a = p[i], b = p[i + 1];
            long long diff = a > b ? a - b : b - a;
            if (diff == gcd(a, b))
                ans++;
        }

        printf("%lld\n", ans);
    }

    return 0;
}