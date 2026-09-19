#include <stdio.h>

int main(){
    int tests; scanf("%d", &tests);
    for(int _ = 0; _ < tests; _++){
        int n, k; scanf("%d %d", &n, &k);
        int Target = n ^ k;

        int num1 = -1, num2 = -1;
        int P = 1;
        if(Target == 0){
      
        } else if(Target < n){
            num1 = Target;
        } else {
            while(P <= n-1){
                P *= 2;
            }
            if(Target >= P){
                printf("NO\n");
                continue;
            }
            num1 = P/2;
            num2 = Target ^ num1;
        }

        printf("YES\n");
        for (int j = 1; j < n; j++) {
            if (j != num1 && j != num2) {
                printf("%d ", j);
            }
        }
        printf("0 ");
        if (num2 != -1) {
            printf("%d ", num2);   
        }
        if (num1 != -1) {
            printf("%d ", num1);   
        }
        printf("\n");
    }
    return 0;
}