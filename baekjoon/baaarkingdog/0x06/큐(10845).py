n = int(input())
q, h, t, p = [0 for _ in range(n)], 0, 0, print

for _ in range(n):
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
        q[t] = c.split().pop()
        t += 1
