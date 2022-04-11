from itertools import groupby
from operator import itemgetter
from math import ceil


def solve(n, k, tickets):
    unpicked = [num for num in range(1, k+1) if num not in tickets]
    intervals = []
    
    for i, g in groupby(enumerate(unpicked), lambda ix : ix[0] - ix[1]):
        intervals.append(list(map(itemgetter(1), g)))

    highest = 0
    mem = 0

    for interval in intervals:
        if len(interval) == 1:
            score = 1
        elif 1 in interval or k in interval:
            score = len(interval)
        else:
            score = ceil(len(interval)/2)

        if score >= highest:
            mem = highest
            highest = score

    total_score = highest + mem

    for interval in intervals:
        if len(interval) > 1 and (1 not in interval or k not in interval):
            score = len(interval)
        if score > total_score:
            total_score = score

    result = total_score/k
    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n, k = list(map(int, input().split()))
        tickets = list(map(int, input().split()))
        result = solve(n, k, tickets)
        print('Case #{}: {}'.format(case, result))