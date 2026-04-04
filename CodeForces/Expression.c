#include <stdio.h>

int main(){

    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);

    int operations[5] = {a+b+c, a*b*c, a+b*c, (a+b)*c, a*(b+c)};

    int max = operations[0];

    for(int i=0; i<5; i++){
        if(operations[i] > max){
            max = operations[i];
        }
    }

    printf("%d", max);

    return 0;
}