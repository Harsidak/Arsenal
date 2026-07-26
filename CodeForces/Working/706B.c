#include <stdio.h>
#include <stdlib.h>

int Bs(int *array, int target){
    int len = sizeof(array) / sizeof(array[0]);
    int low = 0;
    int high = len - 1;
    int ans = -1;

    while(low <= high){
        int mid = low + (high - low) / 2;
        if(array[mid] >= target){
            ans = mid;
            high = mid - 1;
        }else{
            low = mid + 1;
        }
    }
        return ans;
}
int main(){
    int n;
    scanf("%d", &n);
    int arr[n + 1];
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    qsort(arr, n, sizeof(int), compare);

    int q;
    scanf("%d", &q);
    int arr2[q + 1];
    for(int i = 0; i < q; i++){
        scanf("%d", &arr2[i]);

        int count = Bs(arr, arr2[i]);
        printf("%d\n", count);
    }

    return 0;
}
