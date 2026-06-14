#include <stdio.h>

int main(){
    int n;scanf("%d",&n);
    char colors[50];scanf("%s",colors);
    int count=0;
    for(int i=0;i<n-1;i++){
        if(colors[i]==colors[i+1]){
            count++;
        }
    }
    printf("%d",count);

    return 0;
}