n, *A = map(int, open(0).read().split())
x = 1
for a in A:
    x += a == x
print(n-x+1)
