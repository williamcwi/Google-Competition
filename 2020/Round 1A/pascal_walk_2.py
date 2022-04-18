def solve(n):
    if n <= 1000:
        current = 1
        print(1, 1)

        for i in range(1, 46):
            if n - current >= i:
                current += i
                print(i+1, 2)
            else:
                for j in range(i, i+(n-current)):
                    print(j, 1)
                break


if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        print('Case #{}:'.format(case))
        solve(n)