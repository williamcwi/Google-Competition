# TODO: Complete the get_ruler function
def get_ruler(kingdom):
    ruler = ''
    last = kingdom[-1]
    vowels =  ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    ys = ['Y', 'y']
    if last in vowels:
        ruler = 'Alice'
    elif last in ys:
        ruler = 'nobody'
    else:
        ruler = 'Bob'
    return ruler

def main():
    # Get the number of test cases
    t = int(input())
    for case in range(1, t+1):
        # Get the kingdom
        kingdom = input()
        print('Case #{}: {} is ruled by {}.'.format(case, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
  main()
