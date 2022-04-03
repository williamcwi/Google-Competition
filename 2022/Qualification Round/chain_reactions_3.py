def solve(n, fun, point):
    result = 0

    mem_arr = [[] for num in range(n)]
    reversed_order = reversed(range(n))
    for node in reversed_order:
        mem = 0
        if mem_arr[node] != []:
            # print(mem_arr[node])
            mem = min(mem_arr[node])

        val = max(fun[node], mem)

        result += val - mem

        if point[node] > 0:
            mem_arr[point[node] - 1].append(val)


    return result


if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        fun = list(map(int, input().split()))
        point = list(map(int, input().split()))
        result = solve(n, fun, point)
        print('Case #{}: {}'.format(case, result))