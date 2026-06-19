#include <stdio.h>

int main(){
    int t; scanf("%d", &t);
    for(int _ = 0; _ < t; _++){
        int n = 0; scanf("%d", &n);
        int towers[n];
        for(int i = 0; i < n; i++){
            scanf("%d", &towers[i]);
        }

        int current_min = towers[0];
        int sum = 0;
        for(int i = 0; i < n-1; i++){
            if(towers[i] < current_min){
                current_min = towers[i];
            }
            sum += current_min;
        }

        printf("%d\n", sum);
    }
    return 0;
}