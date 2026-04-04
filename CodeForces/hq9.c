#include <stdio.h>

int main(){

    char s[101];
    scanf("%s", s);

    for(int i=0; s[i] != '\0'; i++){

        if(s[i]=='H' || s[i]=='Q' || s[i]=='9'){
            printf("YES");
            return 0;
        }
    }

    printf("NO");

    return 0;
}