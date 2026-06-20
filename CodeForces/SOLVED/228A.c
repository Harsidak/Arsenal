#include <stdio.h>

int main() {
    int s1,s2,s3,s4; scanf("%d %d %d %d", &s1, &s2, &s3, &s4);
    int count = 0;
    if (s1 == s2 || s1 == s3 || s1 == s4) count++;
    if (s2 == s3 || s2 == s4) count++;
    if (s3 == s4) count++;
    printf("%d\n", count);
    return 0;
}