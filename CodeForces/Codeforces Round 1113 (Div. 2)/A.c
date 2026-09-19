#include <stdio.h>
#include <string.h>

void RC(const char* src, int idx, char* dest) {
    int len = strlen(src);
    int k = 0;
    for(int i = 0; i < len; i++) {
        if(i != idx) {
            dest[k++] = src[i];
        }
    }
    dest[k] = '\0';
}

int main(){
    int t; scanf("%d", &t);
    while(t--){
        char s[101]; scanf("%s", s);
        
    }
    return 0;
}