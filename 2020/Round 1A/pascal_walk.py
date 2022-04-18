def solve(n):
    if n <= 501:
        if n == 501:
            print(1, 1)
            print(2, 2)
            print(3, 3)
            print(3, 2)
            print(3, 1)
            for i in range(4, 499):
                print(i, 1)

        else:
            for i in range(1, n+1):
                print(i, 1)

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        print('Case #{}:'.format(case))
        solve(n)