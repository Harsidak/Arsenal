#include <stdio.h>

int main() {
    int tests; 
    if (scanf("%d", &tests) != 1) return 0;
    
    while(tests--) {
        int n;
        scanf("%d", &n);
        int a[n], m[n];
        for(int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }
        for(int i = 0; i < n; i++) {
            scanf("%d", &m[i]);
        }
    
        int c10 = 0, c01 = 0, c11 = 0, c00 = 0;
        for(int i = 0; i < n; i++) {
            if (a[i] != m[i]){
                if (a[i] == 1 && m[i] == 0){
                    c10++;
                }else{
                    c01++;
                }
            }else{
                if(a[i] == 1 && m[i] == 1){
                    c11++;
                }else{
                    c00++;
                }
            }
        }



        if (c10 == 0 && c01 ==0 ){
            printf("%d\n", 0);
        }else if (c10 % 2 !=0){
            printf("%d\n", 1);
        }else if(c10 > 0 && c10 % 2 == 0 ){
            printf("%d\n", 2);
        }else{
            if (c11 > 0 && c00 > 0) {
                printf("2\n");
            } else {
                printf("-1\n");
            }
        }
    }
    return 0;
}