#include <stdio.h>
#include <ctype.h>

int main(){

    char s[101];
    scanf("%s", s);

    for(int i = 0; s[i] != '\0'; i++){

        char c = tolower(s[i]);

        if(c!='a' && c!='o' && c!='y' && c!='e' && c!='u' && c!='i'){
            printf(".%c", c);
        }
    }

    return 0;
}