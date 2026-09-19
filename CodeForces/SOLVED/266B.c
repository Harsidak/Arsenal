#include <stdio.h>

void swap_letter(char *c1, char *c2) {
    char temp = *c1;
    *c1 = *c2;
    *c2 = temp;
}

int main() {
    int n, t; scanf("%d %d", &n, &t);char line[n + 1];scanf("%s", line);

    for (int i = 0; i < t; i++) {
        for (int j = 0; j < n - 1; ) {
            if (line[j] == 'B' && line[j+1] == 'G') {
                swap_letter(&line[j], &line[j+1]);
                j += 2;
            } else {
                j += 1;
            }
        }
    }

    printf("%s\n", line);
    return 0;
}