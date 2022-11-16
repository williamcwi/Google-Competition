#include <stdio.h>

double get_area(int r, int a, int b) {
    int current = r;
    const double pi = 3.14159265358979;
    double area = pi * current * current;

    while (current != 0) {
        current = current * a;
        area += (pi * current * current);
        
        current = current / b;
        area += (pi * current * current);
    }

    return area;
}

int main() {
    int testcases;
    scanf("%d", &testcases);
    int r, a, b;

    for (int t = 1; t <= testcases; ++t) {
            scanf("%d %d %d", &r, &a, &b);
            printf("Case #%d: %lf\n", t, get_area(r, a, b));
    }
    return 0;
}
