#include <stdio.h>
#include <string.h>

char* GetRuler(char* kingdom) {
    // TODO: implement this method to determine the ruler name, given the kingdom.
    char* ruler = "";
    char* vowels = "AEIOUaeiou";
    char* ys = "Yy";
    char last;

    last = kingdom[strlen(kingdom)-1];
    if (strchr(vowels, last) != NULL) {
        ruler = "Alice";
    } else if (strchr(ys, last) != NULL) {
        ruler = "nobody";
    } else {
        ruler = "Bob";
    }

    return ruler;
}

int main() {
    int testcases;
    scanf("%d", &testcases);
    char kingdom[100];

    for (int t = 1; t <= testcases; ++t) {
            scanf("%s", &kingdom);
            printf("Case #%d: %s is ruled by %s.\n", t, kingdom, GetRuler(kingdom));
    }
    return 0;
}
