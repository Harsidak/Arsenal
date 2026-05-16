#include <stdio.h>

int main() {
    int a,b;scanf("%d %d",&a,&b);
    int count = 0;
    while(a<=b) {
        a = a*3;
        b <<= 1;
        count++;
    }
    printf("%d",count);
    return 0;
}