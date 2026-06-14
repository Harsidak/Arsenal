#include <stdio.h>

int main(){
    int n,a,b,c,r=0;
    scanf("%d",&n);
    while(n--) scanf("%d%d%d",&a,&b,&c), r+=a+b+c>1;
    printf("%d",r);
}