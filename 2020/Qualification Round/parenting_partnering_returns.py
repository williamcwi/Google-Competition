def solve(n):
    result = []

    schedule = []
    for _ in range(n):
        schedule.append(list(map(int, input().split())))
    
    order = [i[0] for i in sorted(enumerate(schedule), key=lambda x:x[1])]

    schedule.sort()

    c, j = 0, 0

    for activity in schedule:
        if c <= activity[0]:
            result.append('C')
            c = activity[1]
        elif j <= activity[0]:
            result.append('J')
            j = activity[1]
        else:
            result = 'IMPOSSIBLE'
            break

    if result != 'IMPOSSIBLE':
        result = ''.join([x for _, x in sorted(zip(order, result), key=lambda pair: pair[0])])

    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        result = solve(n)
        print('Case #{}: {}'.format(case, result))