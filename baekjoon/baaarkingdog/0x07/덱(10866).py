import sys

i, p = sys.stdin.readline, print
n = int(i().strip())
d = [0] * (n * 2)
h = t = n

for _ in range(n):
    c = i()
    f = "front" in c
    if c[0] == "p":
        if c[1] == "u":
            v = c.split().pop()
            if f:  # push_front
                h -= 1
                d[h] = v
            else:  # push_back
                d[t] = v
                t += 1
        else:
            if h == t:
                p(-1)
            elif f:  # pop_front
                p(d[h])
                h += 1
            else:  # pop_back
                p(d[t - 1])
                t -= 1
    else:
        if "i" in c:  # size
            p(t - h)
        elif "y" in c:  # empty
            p(int(t == h))
        else:
            if h == t:
                p(-1)
            elif f:  # front
                p(d[h])
            else:  # back
                p(d[t - 1])
