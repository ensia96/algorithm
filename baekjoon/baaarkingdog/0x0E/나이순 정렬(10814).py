import sys
i = sys.stdin.readline


def m(l):
    if len(l) == 1:
        return l
    s = len(l)
    t = s // 2
    a, b, c = m(l[:t]), m(l[t:]), []
    i = j = 0
    for _ in range(s):
        if i == t:
            c += [b[j]]
            j += 1
        elif j == s-t:
            c += [a[i]]
            i += 1
        elif a[i][0] <= b[j][0]:
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1
    return c


for a in m([*map(lambda x: (int(x[0]), x[1]), [i().split() for _ in range(int(i()))])]):
    print(*a)
