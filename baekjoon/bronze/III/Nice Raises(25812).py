T = [0]*3
n, r, *A = map(int, open(0).read().split())
for a in A:
    T[(a+r > 2*a)+2*(a+r < 2*a)] += 1
a, b, c = T
print((b > c)+2*(b < c))
