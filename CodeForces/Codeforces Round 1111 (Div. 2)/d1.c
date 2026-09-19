#include <stdio.h>
#include <stdlib.h>

int max(int a, int b) { return (a > b) ? a : b; }
int min(int a, int b) { return (a < b) ? a : b; }

void solve() {
    int n, q;
    scanf("%d %d", &n, &q);

    int *arr = (int *)malloc(n * sizeof(int));
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    int *pm = (int *)malloc(n * sizeof(int));
    pm[0] = arr[0];
    for(int i = 1; i < n; i++) {
        pm[i] = max(pm[i - 1], arr[i]);
    }

    int *sm = (int *)malloc(n * sizeof(int));
    sm[n - 1] = arr[n - 1];
    for(int i = n - 2; i >= 0; i--) {
        sm[i] = min(sm[i + 1], arr[i]);
    }

    int min_k = 0;

    for(int i = 1; i < n; i++) {
        if(pm[i - 1] > sm[i]) {
            int current_k = 1 << __builtin_ctz(i); 
            min_k = max(min_k, current_k);
        }
    }

    printf("%d\n", min_k);

    free(arr);
    free(pm);
    free(sm);
}

int main() {
    int tests; 
    if (scanf("%d", &tests) != 1) return 0;
    
    while(tests--) {
        solve();
    }
    return 0;
}