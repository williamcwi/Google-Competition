import sys

def solve(b):
    result = ''

    for i in range(1, b+1):
        if i % 10 == 1:
            print(i)
            _ = str(input())
        print(i)
        result = result + str(input())

    print(result)
    ok = str(input())
    if ok == 'Y':
        pass
    else:
        sys.exit()

if __name__ == '__main__':
    t, b = list(map(int, input().split()))
    for case in range(1, t+1):
        solve(b)