_, m, *A = map(int, open(0).read().split())
x = 1
for a in A:
    x = x * max(1, a) % m
print(x)
