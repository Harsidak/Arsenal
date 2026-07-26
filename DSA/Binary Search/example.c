#include <stdio.h>

int Bs(int array[], int target){
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
