import urllib.request
import re
import itertools
from operator import itemgetter

url = 'https://codejam.googleapis.com/dashboard/get_file/AQj_6U3PbqYbwiFNAMPP1wOKIuVr4GSkRpG7b59EQpIC8rj-17A-ZkbjiEJqgR20vWN5WZowHUAPq_pX72W9kPRHZAlfCOxx5UQCXNY/moons_and_umbrellas_sample_ts1_input.txt'
file = urllib.request.urlopen(url)

sample_input = []

for line in file:
    decoded_line = line.decode('utf-8')
    sample_input.append(decoded_line.split())

cases = int(sample_input[0][0])

for case in range(1, cases + 1):
    x = int(sample_input[case][0])
    y = int(sample_input[case][1])

    mural = sample_input[case][2]

    # replace ?

    spaceLocation = [m.start() for m in re.finditer('\?', mural)]

    spaceSets = []

    for k, g in itertools.groupby(enumerate(spaceLocation), lambda ix : ix[0] - ix[1]):
        spaceSets.append(list(map(itemgetter(1), g)))

    comb = itertools.product('CJ', repeat=len(spaceSets))

    totalCost = 999999

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

        if totalCost > cost:
            totalCost = cost


    print('Case #{}: {}'.format(case, totalCost))