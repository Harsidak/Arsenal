// write a program to calculate distance between two points in 2D space. distance = sqrt((x2-x1)^2 + (y2-y1)^2)

#include <stdio.h>
#include <math.h>

double calculateDistance(int point1[], int point2[]) {
    int dx = point2[0] - point1[0];
    int dy = point2[1] - point1[1];
    return sqrt(dx * dx + dy * dy);
}

int main() {
    int point1[2], point2[2];
    printf("Enter coordinates of first point (x1 y1): ");
    scanf("%d %d", &point1[0], &point1[1]);
    printf("Enter coordinates of second point (x2 y2): ");
    scanf("%d %d", &point2[0], &point2[1]);
    double result = calculateDistance(point1, point2);
    printf("Distance: %.2f\n", result);
    return 0;
}

