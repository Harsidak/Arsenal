#include <stdio.h>
#include <math.h>

int Cirno(int a,int n,int d[n+1]) {
    int max = d[0]; for (int fgh = 0;fgh<n+1;fgh++){if (max < d[fgh]) max = d[fgh];}
    int min = d[0]; for (int fgh = 0;fgh<n+1;fgh++){if (min > d[fgh]) min = d[fgh];}
    int digits = 0;long long temp = a;
    while (temp != 0) { temp = temp / 10; digits++; }
    long long b_short = 0; // Start at 0, not 1
    for (int i = 0; i < digits - 1; i++) {
        b_short = b_short * 10 + max; // Shifts left and adds!
    }
    long long int min_dist = 2e18;
    int b_long = 0;
    for (int i = 0;i<digits-1;i++) {
        if (min==0) {
            b_long  = max;
            for (int i = 0; i < digits; i++) b_long = b_long * 10 + min;
        }
        else {
        for (int i = 0; i < digits + 1; i++) b_long = b_long * 10 + min; }
    }
    long long int dist = abs(a -b_long);
    if (dist < min_dist) min_dist = dist;

}

int main () {
    int t;scanf("%d",&t);
    for (int i=1;i<=t;i++) {
        long long int a;
        int n; scanf("%lld %d",&a, &n);int d[n];for (int j = 0;j<n;j++) {scanf("%d",&d[j]);}
        Cirno(a,n,d);
    }
    return 0;
}