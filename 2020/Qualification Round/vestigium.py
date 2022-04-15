def solve(n):
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    k = 0
    r = 0
    c = 0

    for i in range(n):
        k += matrix[i][i]

    for i in range(n):
        if len(matrix[i]) != len(set(matrix[i])):
            r += 1
        
    new_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]

    for i in range(n):
        if len(new_matrix[i]) != len(set(new_matrix[i])):
            c += 1

    result = '{} {} {}'.format(k, r, c)
    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        result = solve(n)
        print('Case #{}: {}'.format(case, result))