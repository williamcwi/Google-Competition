def h_index(n, citations):
    result = []

    hindex = 0
    score = hindex + 1

    for i in range(1, n+1):
        count = 0
        for j in citations[0:i]:
            if j >= score:
                count += 1
        if count > hindex:
            hindex = count
            score = hindex + 1
        result.append(str(hindex))

    return ' '.join(result)

def main():
    t = int(input())

    for case in range(1, t+1):
        n = int(input())                      # The number of papers
        citations = list(map(int, input().split())) # The number of citations for each paper
        h_index_scores = h_index(n, citations)
        print('Case #{}: {}'.format(case, h_index_scores))

if __name__ == '__main__':
    main()