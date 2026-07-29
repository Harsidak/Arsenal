#include <stdio.h>

int main() {
    int tests;
    if (scanf("%d", &tests) != 1) return 0;
    
    while (tests--) {
        long long n, k;
        // scanf naturally handles space-separated inputs, 
        // which fixes the ValueError you were getting in Python!
        scanf("%lld %lld", &n, &k);
        
        long long ans = k + (k - 1) / (n - 1);
        printf("%lld\n", ans);
    }
    
    return 0;
}