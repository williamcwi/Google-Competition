import re
import itertools
from operator import itemgetter

def solve(x, y, mural):

    # replace ?

    spaceLocation = [m.start() for m in re.finditer('\?', mural)]

    spaceSets = []

    for k, g in itertools.groupby(enumerate(spaceLocation), lambda ix : ix[0] - ix[1]):
        spaceSets.append(list(map(itemgetter(1), g)))

    comb = itertools.product('CJ', repeat=len(spaceSets))

    result = 999999

    for c in comb:
        for set, i in zip(spaceSets, range(len(c))):
            for s in set:
                list1 = list(mural)
                list1[s] = c[i]
                mural = ''.join(list1)
        
        # find cost

        numOfCJ = len([m.start() for m in re.finditer('(?=CJ)', mural)])
        numOfJC = len([m.start() for m in re.finditer('(?=JC)', mural)])

        cost = numOfCJ * x + numOfJC * y

        if result > cost:
            result = cost

    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        line = list(map(str, input().split()))
        x = int(line[0])
        y = int(line[1])
        mural = str(line[2])
        result = solve(x, y, mural)
        print('Case #{}: {}'.format(case, result))