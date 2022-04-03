import copy

def build_tree(fun, point):
    tree = []
    for val, linked in zip(fun, point):
        tree.append([val, linked])
    return tree

def run_tree(tree, parent_nodes):
    result = 0
    for node in parent_nodes: 
        val = []
        for t in tree:
            if t[1] == node:
                val.append(t[0])
        # print('val: {}'.format(val))
        index_min = min(range(len(val)), key=val.__getitem__)
        # print(index_min)

        for idx, values in enumerate(val):
            if idx == index_min:
                # compare value with parent node
                if values > tree[node-1][0]:
                    tree[node-1][0] = values
                continue
            else: 
                result += values

    for last in tree:
        if last[1] == 0:
            result += last[0]
    # print('results: {}'.format(result))
    return result

def solve(n, fun, point):
    # build tree
    tree = build_tree(fun, point)
    # print(tree)
    parent_nodes = list(set(point))
    parent_nodes.remove(0)
    parent_nodes.sort(reverse=True)
    # print(parent_nodes)

    temp_tree = copy.deepcopy(tree)

    return run_tree(temp_tree, parent_nodes)


if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        fun = list(map(int, input().split()))
        point = list(map(int, input().split()))
        result = solve(n, fun, point)
        print('Case #{}: {}'.format(case, result))