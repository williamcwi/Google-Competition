def solve(line):

    numOfElements = line[0]
    cost = line[1]

    low = numOfElements - 1
    high = int(((numOfElements * (numOfElements + 1)) / 2) - 1)

    if cost < low or cost > high:
        result = 'IMPOSSIBLE'
    else:
        ans = [None] * numOfElements

        iteration = numOfElements - 1

        low = 1
        high = numOfElements

        reverse = []

        for i in range(numOfElements):
            if (cost - numOfElements) >= iteration - 1:
                
                cost = cost - numOfElements
                numOfElements = numOfElements - 1

                ans[high - 1] = low

                ans[low - 1:high] = ans[low - 1:high][::-1]
                reverse.append([low - 1, high])

                low = low + 1

                iteration = iteration - 1
            
            else: 

                cost = cost - 1
                numOfElements = numOfElements - 1

                ans[low - 1] = low

                low = low + 1

                iteration = iteration - 1
        
        for i in reverse[::-1]:
            ans[i[0]:i[1]] = ans[i[0]:i[1]][::-1]

        result = ' '.join(str(e) for e in ans)

    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        line = list(map(int, input().split()))
        result = solve(line)
        print('Case #{}: {}'.format(case, result))