#include <stdio.h>
#include <math.h>
int Momoyo(int n,int k,int a[n+1],int u[n],int v[n]) {


}
int main() {
    int t; scanf("%d",&t);for(int tc=1;tc<=t;tc++) {
        int n,k;scanf("%d %d",&n,&k);
        int a[n+1];for(int ik=1;ik<=n;ik++) scanf("%d",&a[ik]);
        int u[n],v[n];for(int ij=1;ij<=n;ij++) scanf("%d %d",&u[ij],&v[ij]);
        Momoyo(n,k,a,u,v);
    }

    return 0;
}