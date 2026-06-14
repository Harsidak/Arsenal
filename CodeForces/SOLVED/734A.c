#include <stdio.h>

int main() {
    long long int n;char s;scanf("%lld",&n);
    long long int A_count = 0,D_count = 0;

    for (int i=0;i<n;i++) {
        scanf(" %c",&s);
        if (s == 'A') {A_count++;}
        else{D_count++;}
    }
    if (A_count > D_count) {
        printf("Anton");
    }else if (A_count == D_count) {
        printf("Friendship");
    }else {
        printf("Danik");
    }

    return 0;
}