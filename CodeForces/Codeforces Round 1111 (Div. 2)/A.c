#include <stdio.h>

int main(){
    int tests; scanf("%d", &tests);
    for(int _ = 0;_ < tests;_++){
        int n;
        scanf("%d", &n);

        int sum = 0;
        for(int j=1;j<=n;j++){
            int val;
            scanf("%d",&val);
            sum += val;
        }
        
        if(sum % 4 == 0){
            printf("YES\n");
        }else{
            printf("NO\n");
        }
    }
    return 0;
}