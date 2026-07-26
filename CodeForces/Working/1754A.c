#include <stdio.h>

int main() {
    int t; 
    scanf("%d", &t);
    while(t--) {
        int n;
        scanf("%d", &n);
        char s[n+1];
        scanf("%s", s);

        int c = 1;
        for(int i = 1; i < n; i++) {
            if(s[i] == 'Q') {
                c++;
            } else if (c > 0){
                c--;
            }
        }

        if(c == 0) printf("Yes\n");
        else printf("No\n");
    }
    return 0;
}