#include <stdio.h>
#include <stdlib.h>

int Bs(int *array,int len, int target){
    int low = 0;
    int high = len - 1;
    int ans = len;
    while(low <= high){
        int mid = low + (high - low) / 2;
        if(array[mid] > target){
            ans = mid;
            high = mid - 1;
        }else{
            low = mid + 1;
        }
    }
    return ans;
}

int compare(const void *a, const void *b){
    return *(int*)a - *(int*)b;
}

int main(){
    int n;
    scanf("%d", &n);

    int arr[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    qsort(arr, n, sizeof(int), compare);

    int q;
    scanf("%d", &q);

    for(int i = 0; i < q; i++){
        int x;
        scanf("%d", &x);

        printf("%d\n",Bs(arr,n,x));
    }

    return 0;
}