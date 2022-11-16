from math import pi

def solve(r, a, b):
    current = r

    area = pi * current * current

    while current != 0:
        current = current * a
        area += (pi * current * current)

        current = current // b
        area += (pi * current * current)

    return area
    

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        r, a, b = map(int, input().split())
        result = solve(r, a, b)
        print('Case #{}: {}'.format(case, result))