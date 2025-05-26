n, k, *A = map(int, open(0).read().split())
for a in A:
    while a & 1 ^ 1:
        k -= 1
        a //= 2
print(1 ^ (k > 0))
