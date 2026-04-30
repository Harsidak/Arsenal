#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 200005

static int cnt[MAXN];
static int fillers[MAXN];
static int a[MAXN];

static int cmp_int(const void *x, const void *y) {
    return *(int*)x - *(int*)y;
}

int main(void) {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        for (int i = 0; i < n; i++) scanf("%d", &a[i]);

        memset(cnt, 0, n * sizeof(int));

        /* Frequency count for values in [0, n-1] only */
        for (int i = 0; i < n; i++)
            if (a[i] < n) cnt[a[i]]++;

        /* Build filler pool: elements >= n + extra duplicate copies */
        int fc = 0;
        for (int i = 0; i < n; i++)
            if (a[i] >= n) fillers[fc++] = a[i];
        for (int v = 0; v < n; v++)
            for (int j = 1; j < cnt[v]; j++) fillers[fc++] = v;

        qsort(fillers, fc, sizeof(int), cmp_int);

        int ptr = 0, mex = 0;

        for (int v = 0; v < n; v++) {
            if (cnt[v] >= 1) {
                /* Exact match covers v */
                mex = v + 1;
            } else {
                /* Need filler strictly greater than 2v */
                while (ptr < fc && fillers[ptr] <= 2 * v) ptr++;
                if (ptr < fc) {
                    ptr++;
                    mex = v + 1;
                } else {
                    break; /* No valid filler — MEX is v */
                }
            }
        }

        printf("%d\n", mex);
    }

    return 0;
}