// radius is given caclate the ares and circumference of the circle. area = pi * r^2, circumference = 2 * pi * r

#include <stdio.h>
#include <math.h>
#define M_PI 3.14159265358979323846

int area(int r){
    return M_PI * r * r;
}

int circumference(int r){
    return 2 * M_PI * r;
}

int main(){
    int radius;
    printf("Enter the radius of the circle: ");
    scanf("%d", &radius);
    printf("Area of the circle: %d\n", area(radius));
    printf("Circumference of the circle: %d\n", circumference(radius));
    return 0;
}