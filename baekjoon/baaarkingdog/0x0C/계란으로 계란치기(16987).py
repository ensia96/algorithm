n = int(input())
d = [[*map(int, input().split())] for _ in range(n)]
v = [0] * n
r = 0


def b(c):
    global r
    if c == n:
        r = max(r, sum(v))
        return
    f = 0
    if not v[c]:
        s, w = d[c]
        for i in range(n):
            if i != c and not v[i]:
                x, y = d[i]
                d[i][0], d[c][0] = x-w, s-y
                v[i], v[c] = x <= w, s <= y
                b(c+1)
                d[i][0], d[c][0] = x, s
                v[i], v[c] = 0, 0
                f = 1
    if not f:
        b(c+1)


b(0)
print(r)
