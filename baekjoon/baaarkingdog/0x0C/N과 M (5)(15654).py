l, _ = lambda: map(int, input().split()), 0


def b(n, m, l, s=[]):
    if len(s) == m:
        print(*map(str, s))
        return
    for i in l:
        if i not in s:
            b(n, m, l, s+[i])


b(*l(), sorted(l()))
