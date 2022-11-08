def solve(n, x):
    result = 0
    for i in range(1, n): 
        if x[i] <= x[i-1]:
            if len(str(x[i])) == len(str(x[i-1])):
                x[i] = int(str(x[i]) + '0')
                result += 1
            else:
                k = len(str(x[i-1])) - len(str(x[i]))

                if x[i] * (10**k) > x[i-1]:
                    x[i] = x[i] * (10**k)
                    result += k
                
                elif int(str(x[i]) + ('9' * k)) > x[i-1]:
                    x[i] = x[i-1] + 1
                    result += k
                else: 
                    x[i] = x[i] * (10 ** (k+1))
                    result += k+1
    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        x = list(map(int, input().split()))
        result = solve(n, x)
        print('Case #{}: {}'.format(case, result))