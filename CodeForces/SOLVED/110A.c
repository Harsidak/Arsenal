#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);

    int count = 0;

    // Step 1: count lucky digits
    while (n > 0) {
        int digit = n % 10;
        if (digit == 4 || digit == 7) {
            count++;
        }
        n /= 10;
    }

    // Step 2: check if count is lucky
    if (count == 0) {
        printf("NO");
        return 0;
    }

    while (count > 0) {
        int d = count % 10;
        if (d != 4 && d != 7) {
            printf("NO");
            return 0;
        }
        count /= 10;
    }

    printf("YES");
    return 0;
}