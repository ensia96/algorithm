def l(s, c, d, e):
    if d == 6:
        print(*c)
        return
    for i in range(e, k):
        if not v[i]:
            v[i] = 1
            l(s, c+[s[i]], d+1, i)
            v[i] = 0


while 1:
    k, *s = map(int, input().split())
    s, v = [*map(str, s)], [0]*k
    if not k:
        break
    l(s, [], 0, 0)
    print()
