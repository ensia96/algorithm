_, *A = map(int, open(0).read().split())
t = 1
for a in A:
    t = t * 2 - a
    if t < 0:
        break
print([t % 1000000007, 'error'][t < 0])
