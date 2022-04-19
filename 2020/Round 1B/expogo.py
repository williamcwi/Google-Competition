def solve(goal):
    x, y = goal

    if x == 0 and y == 0:
        result = ''
    elif (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
        result = 'IMPOSSIBLE'
    else:
        dist = abs(x) + abs(y)
        if dist == 1:
            if x == 1:
                result = 'E'
            elif x == -1:
                result = 'W'
            elif y == 1:
                result = 'N'
            elif y == -1:
                result = 'S'
        elif dist <= 3:
            # 0/3 or 1/2
            if abs(x) == 0 or abs(x) == 3:
                if x == 3:
                    result = 'EE'
                elif x == -3:
                    result = 'WW'
                elif y == 3:
                    result = 'NN'
                elif y == -3:
                    result = 'SS'
            else:
                if x == 1:
                    result = 'E'
                elif x == -1:
                    result = 'W'
                elif y == 1:
                    result = 'N'
                elif y == -1:
                    result = 'S'

                if x == 2:
                    result += 'E'
                elif x == -2:
                    result += 'W'
                elif y == 2:
                    result += 'N'
                elif y == -2:
                    result += 'S'
        elif dist <= 5:
            # 1/4 or 2/3 or 0/5
            if abs(x) == 1 or abs(x) == 4:
                if x == 1:
                    result = 'W'
                    result += 'E'
                elif x == -1:
                    result = 'E'
                    result += 'W'
                elif y == 1:
                    result = 'S'
                    result += 'N'
                elif y == -1:
                    result = 'N'
                    result += 'S'

                if x == 4:
                    result += 'E'
                elif x == -4:
                    result += 'W'
                elif y == 4:
                    result += 'N'
                elif y == -4:
                    result += 'S'
            elif abs(x) == 2 or abs(x) == 3:
                if x == 3:
                    result = 'W'
                    mem = 'E'
                elif x == -3:
                    result = 'E'
                    mem = 'W'
                elif y == 3:
                    result = 'S'
                    mem = 'N'
                elif y == -3:
                    result = 'N'
                    mem = 'S'

                if x == 2:
                    result += 'E'
                elif x == -2:
                    result += 'W'
                elif y == 2:
                    result += 'N'
                elif y == -2:
                    result += 'S'
                
                result += mem
            
            else:
                if x == 5:
                    result = 'WEE'
                elif x == -5:
                    result = 'EWW'
                elif y == 5:
                    result = 'SNN'
                elif y == -5:
                    result = 'NSS'
        elif dist <= 7:
            # 3/4 or 1/6 or 2/5 or 0/7
            if abs(x) == 3 or abs(x) == 4:
                if x == 3:
                    result = 'EE'
                elif x == -3:
                    result = 'WW'
                elif y == 3:
                    result = 'NN'
                elif y == -3:
                    result = 'SS'
                
                if x == 4:
                    result += 'E'
                elif x == -4:
                    result += 'W'
                elif y == 4:
                    result += 'N'
                elif y == -4:
                    result += 'S'
            elif abs(x) == 1 or abs(x) == 6:
                if x == 1:
                    result = 'E'
                elif x == -1:
                    result = 'W'
                elif y == 1:
                    result = 'N'
                elif y == -1:
                    result = 'S'
                
                if x == 6:
                    result += 'EE'
                elif x == -6:
                    result += 'WW'
                elif y == 6:
                    result += 'NN'
                elif y == -6:
                    result += 'SS'
            elif abs(x) == 2 or abs(x) == 5:
                if x == 5:
                    result = 'E'
                    mem = 'E'
                elif x == -5:
                    result = 'W'
                    mem = 'W'
                elif y == 5:
                    result = 'N'
                    mem = 'N'
                elif y == -5:
                    result = 'S'
                    mem = 'S'
                
                if x == 2:
                    result += 'E'
                elif x == -2:
                    result += 'W'
                elif y == 2:
                    result += 'N'
                elif y == -2:
                    result += 'S'

                result += mem
            
            else:
                if x == 7:
                    result = 'EEE'
                elif x == -7:
                    result = 'WWW'
                elif y == 7:
                    result = 'NNN'
                elif y == -7:
                    result = 'SSS'

    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        goal = list(map(int, input().split()))
        result = solve(goal)
        print('Case #{}: {}'.format(case, result))