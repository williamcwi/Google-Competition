def solve(n, p):
    arr = []
    for _ in range(n):
        x = list(map(int, input().split()))
        arr.append(x)

    final_list = []

    for row in arr:
        row.sort()

    for i in range(len(arr)):
        cost_low = 0
        cost_high = 0
        low = arr[i][0]
        high = arr[i][len(arr[i])-1]
        if i == 0:
            # only check after
            cost_low += low
            cost_high += high

            next_low = arr[i+1][0]
            next_high = arr[i+1][len(arr[i])-1]

            cost_low += min(abs(high-next_low), abs(high-next_high))
            cost_high += min(abs(low-next_low), abs(low-next_high))

        elif i == len(arr) - 1:
            # only check before
            cost_low = abs(mem-low)
            cost_high = abs(mem-high)

        else:
            # check both
            cost_low = abs(mem-low)
            cost_high = abs(mem-high)

            next_low = arr[i+1][0]
            next_high = arr[i+1][len(arr[i])-1]

            cost_low += min(abs(high-next_low), abs(high-next_high))
            cost_high += min(abs(low-next_low), abs(low-next_high))

        if cost_low < cost_high:
            for s in arr[i]:
                final_list.append(s)
            mem = max(arr[i])
        elif cost_low == cost_high:
            mem_arr = [max(arr[i]), min(arr[i])]
            mem_cost = []
            for m in mem_arr:
                if i == len(arr) - 1:
                    # only check before
                    new_cost_low = abs(m-low)
                    new_cost_high = abs(m-high)

                else:
                    # check both
                    new_cost_low = abs(m-low)
                    new_cost_high = abs(m-high)

                    new_next_low = arr[i+1][0]
                    new_next_high = arr[i+1][len(arr[i])-1]

                    new_cost_low += min(abs(high-new_next_low), abs(high-new_next_high))
                    new_cost_high += min(abs(low-new_next_low), abs(low-new_next_high))
                if new_cost_low <= new_cost_high:
                    mem_cost.append(new_cost_low)
                else:
                    mem_cost.append(new_cost_high)
            if mem_cost[0] <= mem_cost[1]:
                for s in arr[i]:
                    final_list.append(s)
                mem = max(arr[i])
            else:
                for s in arr[i][::-1]:
                    final_list.append(s)
                mem = min(arr[i])
        else:
            for s in arr[i][::-1]:
                final_list.append(s)
            mem = min(arr[i])
    
    result = 0
    current = 0
    for j in final_list:
        result += abs(j-current)
        current = j

    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n, p = list(map(int, input().split()))
        result = solve(n, p)
        print('Case #{}: {}'.format(case, result))