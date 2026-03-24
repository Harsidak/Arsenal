#include <stdio.h>

int sum(int x, int y){
    x = x + y;
    printf("%d",x);
    return 0;
}
int subtraction(int x, int y){
    x = x - y;
    printf("%d",x);
    return 0;
}int multiplication(int x, int y){
    x = x * y;
    printf("%d",x);
    return 0;
}int division(int x, int y){
    x = x / y;
    printf("%d",x);
    return 0;
}

void calculator(){
    int input;printf("Enter the Calculation you want to do 1-sum 2-subtraction 3-multiply 4-division"); scanf("%d",&input);
    int x,y;
    printf("/nEnter the values of x and y: ");scanf("%d %d",&x,&y);

    if(input==1){
        sum(x,y);
    }if(input==2){
        subtraction(x,y);
    }if(input==3){
        multiplication(x,y);
    }if(input==4){
        division(x,y);
    }
}

int main(){
    calculator();
    return 0;
}