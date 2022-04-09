def solve(word):

    result = ''
    for char in word[::-1]:
        result = min(char+result, char+char+result)
    
    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        word = input()
        result = solve(word)
        print('Case #{}: {}'.format(case, result))