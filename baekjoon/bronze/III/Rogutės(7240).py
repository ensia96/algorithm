n, s, *A = map(int, open(0).read().split())
t = 0
for a in A:
    t += a-(t > s)
print(t)
