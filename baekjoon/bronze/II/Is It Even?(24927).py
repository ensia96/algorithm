n, k, *A = map(int, open(0).read().split())
x = 1
for a in A:
    x *= a
print(1 ^ bool(x % 2**k))
