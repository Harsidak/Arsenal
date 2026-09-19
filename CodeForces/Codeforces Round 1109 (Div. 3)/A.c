#include <stdio.h>
#include <string.h>

int main(){
    int tests; scanf("%d",&tests);
    for(int i = 0;i < tests;i++){
        int n; scanf("%d",&n);
        
        char line[n+1]; scanf("%s",line);

        int current = 0, max_len = 0;
        for (int j = 0; j <= n; j++) {
            if (j < n && line[j] == '#') {
                current++;
            } else {
                if (current > max_len) max_len = current;
                current = 0;
            }
        }

        printf("%d\n",(max_len + 1)/2);

    }
    return 0;
}