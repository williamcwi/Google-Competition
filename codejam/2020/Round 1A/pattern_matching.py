def solve(n):
    suffix = []
    prefix = []
    middle = []
    multiple = []

    current_suffix = ''
    current_prefix = ''

    impossible = False

    for _ in range(n):
        pattern = str(input())
        if pattern.count('*') == 1:
            if pattern.startswith('*'):
                suffix.append(pattern)
            elif pattern.endswith('*'):
                prefix.append(pattern)
            else:
                middle.append(pattern)
        else:
            multiple.append(pattern)
    
    if middle:
        for mid in middle:
            pre, suf = mid.split('*')
            suf = '*' + suf
            pre = pre + '*'
            suffix.append(suf)
            prefix.append(pre)

    if suffix:
        current_suffix = max(suffix, key=len)
        current_suffix = current_suffix[1:]

        for word in suffix:
            if current_suffix.endswith(word[1:]):
                pass
            else:
                impossible = True
    
    if prefix:
        current_prefix = max(prefix, key=len)
        current_prefix = current_prefix[:-1]

        for word in prefix:
            if current_prefix.startswith(word[:-1]):
                pass
            else:
                impossible = True

    if impossible:
        return '*'
    else:
        return current_prefix + current_suffix

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        result = solve(n)
        print('Case #{}: {}'.format(case, result))