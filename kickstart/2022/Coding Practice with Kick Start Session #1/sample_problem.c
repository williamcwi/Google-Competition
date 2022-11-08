#include <stdio.h>

int main(void) {
    int cases;
    scanf("%d", &cases);
    for (int c=1; c<=cases; c++) {
        int N, M, bag, result;
        scanf("%d", &N);
        scanf("%d", &M);
        int sum = 0;
        for (int i=1; i<=N; i++) {
            scanf("%d", &bag);
            sum += bag;
        }
        result = sum % M;
        printf("Case #%d: %d\n", c, result);
    }
}