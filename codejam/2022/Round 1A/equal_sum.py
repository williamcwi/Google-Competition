def solve():

    n = int(input())

    binary = [2**i for i in range(30)]
    remaining = [10**9-i for i in range(n-30)]
    a = binary + remaining

    print(*a, flush=True)

    b = list(map(int, input().split()))

    x, y = [], []

    judge = b + remaining

    for i in judge:
        if sum(x) >= sum(y):
            y.append(i)
        else: 
            x.append(i)
    
    for i in binary[::-1]:
        if sum(x) >= sum(y):
            y.append(i)
        else: 
            x.append(i)

    print(*x, flush=True)

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        solve()