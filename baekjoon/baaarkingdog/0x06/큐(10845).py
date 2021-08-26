q, h, t, p = [], 0, 0, print

for _ in range(int(input())):
    c = input()
    if c == "pop":
        if h == t:
            p(-1)
        else:
            p(q[h])
            h += 1
    elif c == "size":
        p(t - h)
    elif c == "empty":
        p(int(h == t))
    elif c == "front":
        p(q[h])
    elif c == "back":
        p(q[t - 1])
    else:
        q += [c.split().pop()]
        t += 1
        if h > t:
            h = t
