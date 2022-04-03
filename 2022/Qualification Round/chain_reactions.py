from itertools import permutations
import copy


def build_tree(fun, point):
    tree = []
    for val, linked in zip(fun, point):
        tree.append([val, linked])
    return tree

def initiator(point):
    triggers = []
    for i in range(1, len(point)+1):
        if i not in point:
            triggers.append(i)
    return triggers

def find_perm(triggers):
    perm = permutations(triggers)
    return list(perm)

def run_tree(tree, order):
    total_fun = 0
    for node in order:
        fun = []
        val = tree[node-1][0]
        points_to = tree[node-1][1]
        fun.append(val)
        while points_to is not 0:
            # set points_to to 0
            temp_points = points_to
            
            val = tree[points_to-1][0]
            points_to = tree[points_to-1][1]
            fun.append(val)

            for t in tree:
                if t[1] == temp_points:
                    t[1] = 0

            
        total_fun += max(fun)
    return total_fun




def solve(n, fun, point):
    result = 0

    # build tree
    tree = build_tree(fun, point)

    # find initiator
    triggers = initiator(point)

    # find all permutations
    perm = find_perm(triggers)

    temp_tree = copy.deepcopy(tree)

    result = 0

    # run tree
    for trigger_order in perm:
        temp_tree = copy.deepcopy(tree)
        fun = run_tree(temp_tree, trigger_order)
        if fun > result:
            result = fun

    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        fun = list(map(int, input().split()))
        point = list(map(int, input().split()))
        result = solve(n, fun, point)
        print('Case #{}: {}'.format(case, result))