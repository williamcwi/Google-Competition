def solve(card):
    result = ''
    r, c = card[0], card[1]
    edge = '+'
    mid = '|'
    for col in range(c):
        edge = edge+'-+'
        mid = mid+'.|'
    first = list(edge)
    second = list(mid)
    first[0] = '.'
    first[1] = '.'
    second[0] = '.'
    first = ''.join(first)
    second = ''.join(second)
    first_row = True
    for row in range(r):
        if first_row:
            result = result + first
            result = result + '\n'
            result = result + second
            result = result + '\n'
            result = result + edge
            first_row = False
        else: 
            result = result + '\n'
            result = result + mid
            result = result + '\n'
            result = result + edge
    
    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        card = list(map(int, input().split()))
        result = solve(card)
        print('Case #{}: \n{}'.format(case, result))