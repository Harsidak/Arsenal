#include <stdio.h>
#include <math.h>

float area(int a, int b,int c){
    int s = (a+b+c)/2;
    float area = sqrt(s*(s-a)*(s-b)*(s-c));
    return area;
}

int main(){
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    printf("Area of triangle: %f", area(a, b, c));
    return 0;
}