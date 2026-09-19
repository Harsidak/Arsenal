#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);

    long long ans;

    if (n % 2 == 0)
        ans = n / 2;
    else
        ans = -(n + 1) / 2;

    printf("%lld\n", ans);

    return 0;
}