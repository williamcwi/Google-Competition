import urllib.request

url = 'https://codejam.googleapis.com/dashboard/get_file/AQj_6U0EtMCjGToGmQv7SPkCLI9s6BjlJ4beemcz3ip15OZehkZ10NgcOEB1AwiHWSUUZ5_G9pEGAmqU70oZzJpolOlaNPXhewMtn1WUMg/reversort_engineering_sample_ts1_input.txt'
file = urllib.request.urlopen(url)

sample_input = []

for line in file:
    decoded_line = line.decode('utf-8')
    sample_input.append(list(map(int, decoded_line.split())))

cases = sample_input[0][0]

for case in range(1, cases + 1):
    numOfElements = sample_input[case][0]
    cost = sample_input[case][1]

    low = numOfElements - 1
    high = int(((numOfElements * (numOfElements + 1)) / 2) - 1)

    if cost < low or cost > high:
        string = 'IMPOSSIBLE'
    else:
        ans = [None] * numOfElements

        iteration = numOfElements - 1

        low = 1
        high = numOfElements

        reverse = []

        for i in range(numOfElements):
            if (cost - numOfElements) >= iteration - 1:
                
                cost = cost - numOfElements
                numOfElements = numOfElements - 1

                ans[high - 1] = low

                ans[low - 1:high] = ans[low - 1:high][::-1]
                reverse.append([low - 1, high])

                low = low + 1

                iteration = iteration - 1
            
            else: 

                cost = cost - 1
                numOfElements = numOfElements - 1

                ans[low - 1] = low

                low = low + 1

                iteration = iteration - 1
        
        for i in reverse[::-1]:
            ans[i[0]:i[1]] = ans[i[0]:i[1]][::-1]

        string = ' '.join(str(e) for e in ans)


    print('CASE #{}: {}'.format(case, string))