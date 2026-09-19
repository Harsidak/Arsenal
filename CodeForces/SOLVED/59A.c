#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
    char word[100];scanf("%s", word);
    int upper =0, lower =0;


    for(int i =0;i<strlen(word);i++){
        if(islower(word[i])){lower++;}else{upper++;}
    }
    
    for(int j = 0;j<strlen(word);j++){
        if(upper>lower){
            word[j] = toupper(word[j]);
        }else{
            word[j] = tolower(word[j]);
        }
    }

    printf("%s",word);

    return 0;
}