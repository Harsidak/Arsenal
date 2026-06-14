#include <stdio.h>

int arrange_carder(int n,int c[n+1]) {

}

int main() {
    int t; scanf("%d",&t);for(int tc=1;tc<=t;tc++) {
        int n;
        int c[n+1];
        scanf("%d",&n);
        for(int i=1;i<=n;i++) {
            scanf("%d",&c[i]);
        }
        arrange_carder(n,c);
    }
    return 0;
}