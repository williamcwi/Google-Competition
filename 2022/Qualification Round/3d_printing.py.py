def solve(cartridges_a, cartridges_b, cartridges_c):
    cyan = [cartridges_a[0], cartridges_b[0], cartridges_c[0]]
    magenta = [cartridges_a[1], cartridges_b[1], cartridges_c[1]]
    yellow = [cartridges_a[2], cartridges_b[2], cartridges_c[2]]
    black = [cartridges_a[3], cartridges_b[3], cartridges_c[3]]
    min_cyan = min(cyan)
    min_magenta = min(magenta)
    min_yellow = min(yellow)
    min_black = min(black)

    total = 1000000

    result = []

    if min_cyan >= total:
        result.append(str(total))
        total = 0
    else: 
        result.append(str(min_cyan))
        total -= min_cyan
    
    if min_magenta >= total:
        result.append(str(total))
        total = 0
    else: 
        result.append(str(min_magenta))
        total -= min_magenta
    
    if min_yellow >= total:
        result.append(str(total))
        total = 0
    else: 
        result.append(str(min_yellow))
        total -= min_yellow
    
    if min_black >= total:
        result.append(str(total))
        total = 0
    else: 
        result.append(str(min_black))
        total -= min_black

    if total != 0:
        result = 'IMPOSSIBLE'
    else: 
        result = ' '.join(result)

    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        cartridges_a = list(map(int, input().split()))
        cartridges_b = list(map(int, input().split()))
        cartridges_c = list(map(int, input().split()))
        result = solve(cartridges_a, cartridges_b, cartridges_c)
        print('Case #{}: {}'.format(case, result))