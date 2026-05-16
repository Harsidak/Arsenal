#include <stdio.h>

int main() {
    int k,w,n; scanf("%d",&k);scanf("%d",&w);scanf("%d",&n);
    int total =0;
    for (int i = 1; i<=n; i++) {
        total += k*i;
    }
    int left = total - w;
    if (left < 0) printf("%d",0);
    else printf("%d",left);
    // printf("%d\n",left);
    return  0;
}