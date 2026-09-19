#include <stdio.h>

int main(){
    int tests; scanf("%d", &tests);
    for(int _ = 0;_ < tests;_++){
        int n;
        scanf("%d", &n);

        int arr[n+1];
        for(int i = 0;i < n;i++){
            scanf("%d", &arr[i]);
        }

        if ((n & 1) == 1){
            printf("NO\n");
            continue;
        }
        int max_even = -1;
        int m_o = 2000000000;
        
        for(int i = 0;i < n;i++){
            if (i % 2 == 1){
                if (arr[i] > max_even){
                    max_even = arr[i];
                }
            }else{
                if (arr[i] < m_o){
                    m_o = arr[i];
                }
            }
        }
        if (m_o - max_even >= 2){
            printf("YES\n");
        }else{
            printf("NO\n");
        }
    }
    return 0;
}