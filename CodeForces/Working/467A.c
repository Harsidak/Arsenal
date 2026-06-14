#include <stdio.h>
#include <math.h>


int main() {
    int n; scanf("%d", &n);
    int p[n+1],q[n+1];
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &p[i],&q[i]);
    }
    int count = 0;
    for (int j = 0;j<n;j++) {
        int space = abs(p[j] - q[j]);
        if (space >=2) {
            count++;
        }
    }
    printf("%d",count);
    return 0;
}