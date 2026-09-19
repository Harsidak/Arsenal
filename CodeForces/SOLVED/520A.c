#include <stdio.h>
#include <ctype.h>

int main() {
    int n;
    scanf("%d", &n);

    char word[n + 1];
    scanf("%s", word);

    int seen[26] = {0};

    for (int i = 0; i < n; i++) {
        char c = tolower(word[i]);

        if (c >= 'a' && c <= 'z') {
            seen[c - 'a'] = 1;
        }
    }

    int count = 0;

    for (int i = 0; i < 26; i++) {
        count += seen[i];
    }

    if (count == 26)
        printf("YES\n");
    else
        printf("NO\n");

    return 0;
}