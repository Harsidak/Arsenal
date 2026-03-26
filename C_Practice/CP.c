// create a program using a function to take 5 inputs from the user and in an array and print number of odd and evens number in them. (using function and arryas in parameter)
#include <stdio.h>

void countOddEven(int arr[], int size, int *oddCount, int *evenCount) {
    *oddCount = 0;
    *evenCount = 0;

    for (int i = 0; i < size; i++) {
        if (arr[i] % 2 == 0) {
            (*evenCount)++;
        } else {
            (*oddCount)++;
        }
    }
}

int main() {
    int numbers[5];
    int oddCount, evenCount;

    printf("Enter 5 numbers:\n");
    for (int i = 0; i < 5; i++) {
        scanf("%d", &numbers[i]);
    }

    countOddEven(numbers, 5, &oddCount, &evenCount);

    printf("Number of odd numbers: %d\n", oddCount);
    printf("Number of even numbers: %d\n", evenCount);

    return 0;
}

// if we create a variable by both local and global scope
int globalVar = 10; // global variable

int main() {
    int localVar = 20; // local variable
    printf("Global variable: %d\n", globalVar);
    printf("Local variable: %d\n", localVar);
    return 0;
}