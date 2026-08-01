#include <stdio.h>
#include <string.h>

int main(){
    int te; scanf("%d" , &te);
    while(te--){
        int n, q; scanf("%d %d" , &n, &q);
        char s[n+1]; scanf("%s" ,s);
        char t[n+1]; scanf("%s" ,t);
   

        int p1[n + 1];
        int p2[n + 1];

        p1[0] = 0;
        p2[0] = 0;
        for (int i = 0; i < n; i++) {
            int is01 = (s[i] == '0' && t[i] == '1');
            int is10 = (s[i] == '1' && t[i] == '0');

            p1[i + 1] = p1[i] + is01;
            p2[i + 1] = p2[i] + is10;
        }

        for (int i = 0; i < q; i++) {
            int l, r;
            scanf("%d %d", &l, &r);

            int len = r - l + 1;
            int cnum1 = p1[r] - p1[l - 1];
            int cnum2 = p2[r] - p2[l - 1];

            if (2 * cnum1 <= len && 2 * cnum2 <= len) {
                printf("YES\n");
            } else {
                printf("NO\n");
            }
        }
    }
    return 0;
}