#include <stdio.h>
#include <string.h>

void reverse(char *str) {
    int left = 0, right = strlen(str) - 1;

    while (left < right) {
        char temp = str[left];
        str[left] = str[right];
        str[right] = temp;
        left++;
        right--;
    }
}

int main() {
    char bir[101];
    char ber[101];

    scanf("%100s", bir);
    scanf("%100s", ber);

    // Fast fail
    if (strlen(bir) != strlen(ber)) {
        printf("NO");
        return 0;
    }

    reverse(bir);

    if (strcmp(bir, ber) == 0) {
        printf("YES");
    } else {
        printf("NO");
    }

    return 0;
}