def solve(string):

    current = 0
    result = ''
    
    for i in string:
        if int(i) > current:
            diff = int(i) - current
            result = result + ('('*diff)
            result = result + i
            current = int(i)
        elif current > int(i):
            diff = current - int(i)
            result = result + (')'*diff)
            result = result + i
            current = int(i)
        else:
            result = result + i
    result = result + (')'*current)

    return result


if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        string = str(input())
        result = solve(string)
        print('Case #{}: {}'.format(case, result))