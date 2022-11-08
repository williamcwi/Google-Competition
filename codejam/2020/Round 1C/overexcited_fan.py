def reachable(x, y, r):
    if abs(x) + abs(y) <= r:
        return True
    else:
        return False

def solve(X, Y, M):

    if X == 0 and Y == 0:
        return 0

    x = X
    y = Y
    
    for i, m in enumerate(M):
        if m == 'S':
            y -= 1
        elif m == 'N':
            y += 1
        elif m == 'W':
            x -= 1
        elif m == 'E':
            x += 1
        
        r = i + 1

        if reachable(x, y, r):
            return r
    
    return 'IMPOSSIBLE'

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        X, Y, M = list(input().split())
        result = solve(int(X), int(Y), str(M))
        print('Case #{}: {}'.format(case, result))