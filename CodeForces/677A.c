#include <stdio.h>

int main() {
    int n,h; scanf("%d",&n); scanf("%d",&h);
    int a[n];for (int i = 0; i < n; i++) scanf("%d",&a[i]);
    int width = 0;

    for (int j = 0; j < n; j++) {
        if (a[j] > h) {
            width+=2;
        }else {
            width ++;
        }
    }
    printf("%d",width);
    return 0;
}