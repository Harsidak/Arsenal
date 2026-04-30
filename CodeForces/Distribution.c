#include <stdio.h>

#define MOD 676767677LL

int main(void) {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        int a[105];
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);

        long long sum    = 0;
        int last_ge2     = -1;
        int has_one      = 0;

        for (int i = 0; i < n; i++) {
            if (a[i] >= 2) {
                sum = (sum + a[i]) % MOD;
                last_ge2 = i;
            } else {
                has_one = 1;
            }
        }

        if (has_one) {
            int unabsorbable = 0;

            if (last_ge2 == -1) {
                /* All elements are 1 — must cost at least 1 */
                unabsorbable = 1;
            } else {
                /* Any 1 sitting after the last ≥2 element cannot be paired */
                for (int i = last_ge2 + 1; i < n; i++) {
                    if (a[i] == 1) { unabsorbable = 1; break; }
                }
            }

            sum = (sum + unabsorbable) % MOD;
        }

        printf("%lld\n", sum);
    }

    return 0;
}