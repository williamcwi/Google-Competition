def solve(i, p):
    
    result = 0
    while i and p:
        if i[0] == p[0]:
            i.pop(0)
            p.pop(0)
        else: 
            p.pop(0)
            result += 1
    
    if i:
        return "IMPOSSIBLE"
    else:
        return result + len(p)



if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        i = list(input())
        p = list(input())
        result = solve(i, p)
        print('Case #{}: {}'.format(case, result))