def solve(n, d):
    result = 0
    current = 0
    left = 0
    right = n-1

    for _ in range(n):
        low = min(d[left], d[right])
        
        if low >= current:
            result += 1
            current = low
    
        if low == d[left]:
            left += 1
        else:
            right -= 1

    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        d = list(map(int, input().split()))
        result = solve(n, d)
        print('Case #{}: {}'.format(case, result))