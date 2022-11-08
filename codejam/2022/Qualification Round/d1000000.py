def solve(n, sides):
    sides.sort()
    result = 0
    for die in sides:
        if die > result:
            result += 1
    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        sides = list(map(int, input().split()))
        result = solve(n, sides)
        print('Case #{}: {}'.format(case, result))