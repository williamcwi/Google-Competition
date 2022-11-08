def solve(n, d):
    result = 0
    current = 0

    for _ in range(n-1):
        first = d[0]
        last = d[len(d)-1]

        if first <= last:
            low = first
        else:
            low = last

        d.remove(low)
        
        if low >= current:
            result += 1
            current = low

    last = d[0]

    if last >= current:
        result += 1
    
    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        d = list(map(int, input().split()))
        result = solve(n, d)
        print('Case #{}: {}'.format(case, result))