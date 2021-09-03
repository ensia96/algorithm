m = [input().strip() for _ in range(5)]
w, v, p = 0, [[0]*5 for _ in range(5)], []


def c(s):
    x, y = s % 5, s//5
    for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if 0 <= a < 5 and 0 <= b < 5 and not v[b][a] and (b*5+a) in p:
            v[b][a] = 1
            c((b*5+a))


def d(l, i, n):
    global w, v, p
    if n >= 4 or 25-i < 7-l:
        return
    if l == 7:
        c(p[0])
        w += sum(sum(v, [])) == 7
        v = [[0]*5 for _ in range(5)]
        return
    x, y = i % 5, i // 5
    p += [i]
    d(l+1, i+1, n+1 if m[y][x] == 'Y' else n)
    p.pop()
    d(l, i+1, n)


d(0, 0, 0)
print(w)
