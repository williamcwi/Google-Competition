def solve(n, p):
    arr = []
    for _ in range(n):
        x = list(map(int, input().split()))
        arr.append((min(x), max(x)))

    low = [-1] * n
    high = [-1] * n

    low[0] = abs(0 - arr[0][0]) + abs(arr[0][0] - arr[0][1])
    high[0] = abs(0 - arr[0][1]) + abs(arr[0][0] - arr[0][1])

    for i in range(1, n):
        low[i] = min((low[i-1] + abs(arr[i-1][1]-arr[i][0]) + abs(arr[i][0] - arr[i][1])), (high[i-1] + abs(arr[i-1][0]-arr[i][0]) + abs(arr[i][0] - arr[i][1])))
        high[i] = min((low[i-1] + abs(arr[i-1][1] - arr[i][1]) + abs(arr[i][1] - arr[i][0])), (high[i-1] + abs(arr[i-1][0] - arr[i][1]) + abs(arr[i][1] - arr[i][0])))
        
    result = min(low[n-1], high[n-1])
    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n, p = list(map(int, input().split()))
        result = solve(n, p)
        print('Case #{}: {}'.format(case, result))