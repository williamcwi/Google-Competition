def get_factors(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

def check_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

def solve(a):
    result = 0
    factors = get_factors(a)
    for i in factors:
        if check_palindrome(i):
            result += 1
    return result

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        a = int(input())
        result = solve(a)
        print('Case #{}: {}'.format(case, result))