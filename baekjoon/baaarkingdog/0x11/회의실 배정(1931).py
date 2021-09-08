l, i = lambda x: (x[1], x[0]), input
m = sorted([[*map(int, i().split())] for _ in range(int(i()))], key=l)
t, c = m[0][1], 1
for s, e in m[1:]:
    if s >= t:
        t, c = e, c+1
print(c)
