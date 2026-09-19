#include <stdio.h>

int main() {
    int n,a,b;scanf("%d",&n);

    int capacity = 0;
    int max = 0;
    for (int i=0;i<n;i++) {
        scanf("%d %d",&a,&b);
        capacity += b;
        capacity -= a;
        if (max < capacity) max = capacity;
    }
    // printf("%d\n",capacity);
    printf("%d\n", max);

    return 0;
}