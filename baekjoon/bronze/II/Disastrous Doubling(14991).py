_, *A = map(int, open(0).read().split())
t = 1
for a in A:
    t = t * 2 - a % 1000000007
    if t < 0:
        t = 'error'
        break
print(t)
