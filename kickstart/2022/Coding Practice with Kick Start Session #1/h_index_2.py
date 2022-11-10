import heapq

def h_index(n, citations):
    minH = []
    result = []
    hindex = 0

    for i in range(n):
        if citations[i]>hindex:
            heapq.heappush(minH, citations[i])
        while minH and minH[0] <= hindex:
            heapq.heappop(minH)
        if len(minH) >= hindex+1:
            hindex += 1
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