import urllib.request

url = 'https://codejam.googleapis.com/dashboard/get_file/AQj_6U2NygYR7uGzZZteyMk6bvSCzfYtZZFC82WxgjT6ePPbHzdzSXfRoXMaOJAcRorsLQdkhpzqk_DJeVGy9o_BCg/reversort_sample_ts1_input.txt'
file = urllib.request.urlopen(url)

sample_input = []

for line in file:
    decoded_line = line.decode('utf-8')
    sample_input.append(list(map(int, decoded_line.split())))

print(sample_input)

cases = sample_input[0][0]

for case in range(cases):
    numOfElements = sample_input[case * 2 + 1]
    elements = sample_input[case * 2 + 2]

    caseCost = 0

    for i in range(1, numOfElements[0]):

        j = min(range(len(elements[i-1:])), key=elements[i-1:].__getitem__) + i

        elements[i-1:j] = elements[i-1:j][::-1]

        cost = j - i + 1
        caseCost += cost

    print('Case #{}: {}'.format(case + 1, caseCost))