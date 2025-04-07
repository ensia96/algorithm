n, d, k, *A = map(int, open(0).read().split())
a = c = 0
t = max(A)
for _ in " " * d:
    c += t
    if c > k:
        c = t
        a += 1
print(a)
