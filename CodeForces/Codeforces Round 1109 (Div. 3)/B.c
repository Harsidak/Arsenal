#include <stdio.h>
#include <stdlib.h>


int main(){
    int tests; scanf("%d",&tests);
    for(int q = 0;q < tests;q++){
        int n; scanf("%d",&n);
        long long a[200005];
        for(int _ = 0;_ < n;_++){scanf("%lld",&a[_]);}

        long long prefix = 0;
        int indeed = 1;
        for(int i = 0;i < n;i++){
            prefix += a[i];
            long long need  = (long long)(i + 1) * (i+2) / 2;
            
            if(prefix < need){
                indeed = 0;
            }

        }
       if(indeed){
         printf("%s\n","YES");
       }else{
         printf("%s\n","NO");
       }
    }
    return 0;
}