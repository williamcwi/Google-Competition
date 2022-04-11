from itertools import permutations

def solve(time):
    a, b, c = time

    for h, m, s in permutations([a, b, c]):
        
        H, H_rem = h // (60*60*10**9), h % (60*60*10**9)
        M, M_rem = m // (60*12*10**9), m % (60*12*10**9)
        S, N = s // (60*12*10**9), s % (60*12*10**9)

        if int(H_rem/(60*10**9)) == M and int(M_rem/(12*10**9)) == S:
            result = '{} {} {} {}'.format(H, M, S, N)
            return result
    

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        time = list(map(int, input().split()))
        result = solve(time)
        print('Case #{}: {}'.format(case, result))