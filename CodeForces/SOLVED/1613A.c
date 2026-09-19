#include <stdio.h>
#include <stdlib.h>

int isValid(int num, long long int arr[], long long int k, long long int h){

    long long int damage = 0;

    for(int i = 0; i < num - 1; i++){
        long long int gap = arr[i + 1] - arr[i];

        if (gap <= k){
            damage += gap;
        }else{
            damage += k;
        }

        if (damage >= h){
            return 1;
        }
    }
    damage += k;
    return damage >= h ? 1 : 0;
}

long long int bs(long long int arr[], long long int length, long long int h){
    long long int low = 1;
    long long int high = h;
    long long int ans = -1;

    while(low <= high){
        long long int mid = low + (high - low) / 2;

        if(isValid(length, arr, mid, h)){
            ans = mid;
            high = mid - 1;
        }else{
            low = mid + 1;
        }
    }

    return ans;
}

int main(){
    int t;scanf("%d", &t);
    while(t--){
        int n;
        long long int h;
        scanf("%d %lld",&n,&h);

        long long int arr[n];
        for(int i = 0;i < n;i++){scanf("%lld", &arr[i]);}

        printf("%lld\n", bs(arr, n, h));
    }
    return 0;
}