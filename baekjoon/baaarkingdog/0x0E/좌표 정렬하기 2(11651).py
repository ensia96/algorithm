import sys
i = sys.stdin.readline


def m(l):
    if len(l) == 1:
        return l
    s = len(l)
    c = s//2
    a, b, t = m(l[:c]), m(l[c:]), []
    i = j = 0
    for _ in range(s):
        if j == s-c:
            t += [a[i]]
            i += 1
        elif i == c:
            t += [b[j]]
            j += 1
        elif a[i][1] < b[j][1]:
            t += [a[i]]
            i += 1
        elif b[j][1] < a[i][1]:
            t += [b[j]]
            j += 1
        elif a[i][0] < b[j][0]:
            t += [a[i]]
            i += 1
        else:
            t += [b[j]]
            j += 1
    return t


for s in m([[*map(int, i().split())] for _ in range(int(i()))]):
    print(*s)
