l = [0 for _ in range(10)]

for c in input():
    l[int(c)] += 1

print(l)

m, n, o = max(l), l[6], l[9]

if m == n or m == o:
    m = (n + o) // 2 + (n + o) % 2

print(m)
