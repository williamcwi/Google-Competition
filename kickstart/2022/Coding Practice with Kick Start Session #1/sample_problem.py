def solve(n, m, c):
    sum = 0
    for candy in c:
        sum += candy
    result = sum % m
    return result


if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        line = list(map(int, input().split()))
        n = int(line[0])
        m = int(line[1])
        c = list(map(int, input().split()))
        result = solve(n, m, c)
        print('Case #{}: {}'.format(case, result))