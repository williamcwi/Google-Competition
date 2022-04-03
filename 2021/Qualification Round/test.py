def solve(numOfElements, elements):
    caseCost = 0

    for i in range(1, numOfElements[0]):

        j = min(range(len(elements[i-1:])), key=elements[i-1:].__getitem__) + i

        elements[i-1:j] = elements[i-1:j][::-1]

        cost = j - i + 1
        caseCost += cost

    print('Case #{}: {}'.format(case + 1, caseCost))

cases = int(input())
for case in range(cases):
    numOfElements = int(input())
    elements = []
    for e in range(numOfElements):
        elements.append(int(input()))
    solve(numOfElements, elements)