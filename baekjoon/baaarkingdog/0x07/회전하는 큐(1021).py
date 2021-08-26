import collections as c

i = input

n, m = map(int, i().split())
d, a = c.deque([*range(1, n + 1)]), 0

for p in map(int, i().split()):
    c, s = 0, len(d)
    while c < s:
        if d[0] == p:
            break
        d.rotate()
        c += 1
    a += min(s - c, c)
    d.popleft()

print(a)
