l = [i + 1 for i in range(20)]

for _ in range(10):
    s, e = map(int, input().split())
    s -= 1
    l = l[:s] + [*reversed(l[s:e])] + l[e:]

print(*l)
