import numpy as np

def solve(a, b):
    
    result = 0
    for i in range(a, b+1):
        x = [int(j) for j in str(i)]
        producti = np.product(x)
        sumi = sum(x)
        if producti % sumi == 0:
            result += 1
    return result


if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        line = list(map(int, input().split()))
        a = line[0]
        b = line[1]
        result = solve(a, b)
        print('Case #{}: {}'.format(case, result))