n, *A = map(int, open(0).read().split())
x = 0
for a in A:
    x = max(x, a-n)
    n -= 1
print(x)
