n, k, *A = map(int, open(0).read().split())
x = y = 0
for a in A:
    if x + a > k:
        y += 1
        x = 0
    x += a
print(y + 1)
