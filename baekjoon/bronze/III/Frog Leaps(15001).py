_, x, *A = map(int, open(0).read().split())
t = 0
for a in A:
    t += (a-x)**2
    x = a
print(t)
