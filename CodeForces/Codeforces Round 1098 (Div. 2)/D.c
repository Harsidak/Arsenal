#include <stdio.h>

int Cirno(int a,int n,int d[n+1]) {

}

int main () {
    int t;scanf("%d",&t);
    for (int i=1;i<=t;i++) {
        int a,n,d[n+1];scanf("%d %d",&a, &n);for (int i = 0;i<n;i++) {scanf("%d",&d[i]);}
        Cirno(a,n,d);
    }
    return 0;
}