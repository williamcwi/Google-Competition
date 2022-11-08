import random

def solve():
    
    string = ''
    for _ in range(8):
        string += str(random.getrandbits(1))

    print(string)

    n = int(input())

    while n != 0:
        if n == -1:
            print('test failed')
            exit()
        else:
            string = '00000000'
            x = random.sample(range(8), n)
            for i in x:
                string = string[0:i] + '1' + string[i+1:]
            print(string)
        n = int(input())


if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        solve()