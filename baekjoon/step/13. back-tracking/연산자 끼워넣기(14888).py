l, n = lambda: map(int, input().split()), int(input())
b, o, t = [*l()], [*l()], []
c, o = len(b), {i: o[i] for i in range(4)}


def l(r, i):
    global t
    if i == c:
        t += [r]
        return
    for d in range(4):
        if o[d]:
            o[d] -= 1
            l([r+b[i], r-b[i], r*b[i], -(-r//b[i]) if r < 0 else r//b[i]][d], i+1)
            o[d] += 1


l(b[0], 1)
print(max(t))
print(min(t))
