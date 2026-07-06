#include <stdio.h>

int main() {
    int n, a, b, c;
    scanf("%d %d %d %d", &n, &a, &b, &c);

    int ans = 0;

for (int x = 0; x <= n / a; x++) {
    for (int y = 0; y <= n / b; y++) {

        int rem = n - a*x - b*y;

        if (rem < 0)
            continue;

        if (rem % c == 0) {
            int z = rem / c;
            int pieces = x + y + z;

            if (pieces > ans)
                ans = pieces;
        }
    }
}

    printf("%d\n", ans);

    return 0;
}