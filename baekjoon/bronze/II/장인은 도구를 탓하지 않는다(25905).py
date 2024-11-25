_, *A = sorted(map(float, open(0).read().split()))
x = 1
for a in A:
    x *= a
print(x / 36288 * 10**8)
