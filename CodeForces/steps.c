#include <stdio.h>

int main(){
    int n, number[100000];scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&number[i]);
    }   

    int current =1;
    int max = 1;

    for(int j=1;j<n;j++){
     if(number[j] >= number[j-1]){
        current++;
     }
     else{
        current = 1;
     }
     if (current>max){
        max =current;
    }
    }
    printf("%d",max);
    return 0;
}