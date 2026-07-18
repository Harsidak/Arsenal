#include <stdio.h>

int main() {
    int tests; 
    if (scanf("%d", &tests) != 1) return 0;
    
    while(tests--) {
        int n, k, m;
        scanf("%d %d %d", &n, &k, &m);
        
        if (k > m) {
            printf("NO\n");
            continue; 
        }

        printf("YES\n");
        
        int ones_count = k - 1;
        long long correction_number = (long long)m - ones_count;

        for (int i = 1; i <= n; i++) {
            if (i % k == 0) {
                printf("%lld ", correction_number); 
            } else {
                printf("1 ");
            }
        }
        printf("\n");
    }
    return 0;
}