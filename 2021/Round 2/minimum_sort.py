def query(start, end):
    print('M {} {}'.format(start, end), flush=True)

def swap(pos1, pos2):
    print('S {} {}'.format(pos1, pos2), flush=True)

def solve(n):
    for i in range(1, n):
        start = i
        end = n
        query(start, end)
        min = int(input())
        if min is not i:
            swap(min, i)
    print('D')
    result = int(input())
    if result is not 1:
        quit()

if __name__ == '__main__':
    t, n = list(map(int, input().split()))
    for case in range(1, t+1):
        solve(n)