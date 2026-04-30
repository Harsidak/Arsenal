#include <stdio.h>

#define INF 1000000000
#define MAXN 200005

// Global array prevents stack overflow and malloc overhead
int a[MAXN];

void solve() {
    int n;
    scanf("%d", &n);

    int min_odd = INF, max_odd = -INF;
    int min_even = INF, max_even = -INF;

    // Step 1: Read input and find global extremes for both parities
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        if (a[i] % 2 != 0) {
            if (a[i] < min_odd) min_odd = a[i];
            if (a[i] > max_odd) max_odd = a[i];
        } else {
            if (a[i] < min_even) min_even = a[i];
            if (a[i] > max_even) max_even = a[i];
        }
    }

    int ok = 1;

    // Step 2: Check for any trapped pairs in Team Even
    int max_exceeding_odd = -1;
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) {
            // If this even is smaller than all odds, AND we previously saw an even 
            // larger than all odds, these two evens are inverted and have no helper.
            if (a[i] < min_odd && max_exceeding_odd > a[i]) {
                ok = 0;
                break;
            }
            // Track the maximum Even seen so far that is bigger than all Odds
            if (a[i] > max_odd) {
                if (a[i] > max_exceeding_odd) {
                    max_exceeding_odd = a[i];
                }
            }
        }
    }

    // Step 3: Check for any trapped pairs in Team Odd
    int max_exceeding_even = -1;
    if (ok) { // Only run if Evens are fine
        for (int i = 0; i < n; i++) {
            if (a[i] % 2 != 0) {
                if (a[i] < min_even && max_exceeding_even > a[i]) {
                    ok = 0;
                    break;
                }
                if (a[i] > max_even) {
                    if (a[i] > max_exceeding_even) {
                        max_exceeding_even = a[i];
                    }
                }
            }
        }
    }

    // Output the verdict
    if (ok) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }
}

int main() {
    int t;
    // Fast standard I/O processing
    if (scanf("%d", &t) == 1) {
        while (t--) {
            solve();
        }
    }
    return 0;
}