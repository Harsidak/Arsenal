#include <stdio.h>

int main() {
    int n; scanf("%d", &n);
    int present[n+1];
    for (int i = 0; i<n; i++) {
        scanf("%d", &present[i]);
    }

    int presents[n+1];
    int giver, reciver;
    for (int j = 0; j<n; j++) {
        giver = j +1;
        reciver = present[j];
        presents[reciver] = giver;
    }
    for (int k = 1; k<=n; k++) {
        printf("%d ", presents[k]);
    }

    printf("\n");
    return 0;
}