import collections

def solve(goal):
    x, y = goal

    if x == 0 and y == 0:
        result = ''
    elif (x + y) % 2 == 0:
        result = 'IMPOSSIBLE'
    else:
        a = collections.deque()
        a.append([0, 0, 1, []])
        result = []

        while a:
            c, r, s, t = a.popleft()
            if c == x and r == y:
                result = ''.join(t)
                break
            if r != y:
                a.append([c,r+s,s*2,t+['N']])
                a.append([c,r-s,s*2,t+['S']])
            if c != x:
                a.append([c-s,r,s*2,t+['W']])
                a.append([c+s,r,s*2,t+['E']])
        
        if not result:
            result = 'IMPOSSIBLE'

    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        goal = list(map(int, input().split()))
        result = solve(goal)
        print('Case #{}: {}'.format(case, result))