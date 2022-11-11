def solve(i, p):
    
    result = 0
    while i and p:
        if i[-1] == p[-1]:
            i.pop()
            p.pop()
        else: 
            p.pop()
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