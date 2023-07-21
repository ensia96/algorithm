_, x, *A = map(int, open(0).read().split())
y = 0
for a in A:
    if x > a:
        x = a
    y += a-x
print(y)
