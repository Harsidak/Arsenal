#include <stdio.h>

static inline void solve() {
    int x, y;
    scanf("%d %d", &x, &y);
    
    // If both x and y are odd, we need at least two short steps, which is not allowed.
    if ((x & 1) && (y & 1)) {
        printf("NO\n");
    } else {
        printf("YES\n");
    }
}

int main() {
    int t;
    if (scanf("%d", &t) == 1) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
