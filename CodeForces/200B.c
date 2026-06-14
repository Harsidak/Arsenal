#include <stdio.h>

int main() {
    int n; scanf("%d", &n);
    int sum = 0;
    int p;
    for (int i = 0; i < n; i++) {
        scanf("%d", &p);
        sum += p;
    }
    float avg = (float)sum/n;
    printf("%f\n", avg);

    return 0;
}