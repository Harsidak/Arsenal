#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){
    int test;
    srand(time(NULL));
    scanf("%d", &test);
    
    for(int _ = 0; _ < test; _++){
        int x = 32767;

        printf("%d\n", x);fflush(stdout);
        
        int o; scanf("%d", &o);if (o == -1) return 0;

        int m0 = 0; 
        long long r1 = rand();
        long long r2 = rand();
        int m1 = ((r1 << 15) ^ r2) & 1073741823;

        m1 |= 1;
        m1 |= (1 << 15);

        printf("%d %d\n",m0,m1);fflush(stdout);
        
        int r; scanf("%d", &r);if( r == -1) return 0;


        int b = 1;
        if ( (r & x) == o || (r | x) == o ){
            b = 0;
        } else{
            b = 1;
        }

        printf("%d\n", b);fflush(stdout);
        
    }
    return 0;
}