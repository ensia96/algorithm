def r(l):
    if len(l) == 1:
        return l
    s = len(l)
    t = s//2
    a, b, c = r(l[:t]), r(l[t:]), []
    i = j = 0
    for _ in range(s):
        if i == t:
            c += [b[j]]
            j += 1
        elif j == s-t:
            c += [a[i]]
            i += 1
        elif a[i] >= b[j]:
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1
    return c


print('\n'.join(map(str, r([int(input()) for _ in range(int(input()))]))))
