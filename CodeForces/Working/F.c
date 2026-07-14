#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int bubbleSort(int *P, int n){
    int sum = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (P[j] > P[j + 1]) {
                    int temp = P[j];
                    P[j] = P[j + 1];
                    P[j + 1] = temp;
                    sum++;
                }
            }
        }
    return sum;
}

int main(){
    int tests; scanf("%d",&tests);
    for(int k = 0;k < tests;k++){
        int n; scanf("%d", &n);
        int P[n]; for(int q = 0;q < n;q++){scanf("%d",&P[q]);}
        
        printf("%d\n",bubbleSort(P,n));

    }
    return 0;
}