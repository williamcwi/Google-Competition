def solve(n, l):

    result = 0

    for i in range(1, n):

        j = min(range(len(l[i-1:])), key=l[i-1:].__getitem__) + i

        l[i-1:j] = l[i-1:j][::-1]

        cost = j - i + 1
        result += cost

    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        l = list(map(int, input().split()))
        result = solve(n, l)
        print('Case #{}: {}'.format(case, result))