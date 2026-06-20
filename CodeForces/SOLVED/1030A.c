#include <stdio.h>

int main(){
    int n; scanf("%d",&n);
    int N;
    
    int prb = 0;

    for (int i = 0; i < n; i++){
        scanf("%d",&N);
        if(N != 0){
            prb++;   
        }
    }
    
    if (prb>0)
    {
        printf("HARD");
    }else{
        printf("EASY");
    }
    
    
    return 0;
}