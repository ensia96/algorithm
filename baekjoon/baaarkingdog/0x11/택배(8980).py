l, A = lambda: map(int, input().split()), 0
n, c = l()
W = [c]*(n+1)
for f, t, a in sorted([(*l(),)for _ in ' '*int(input())], key=lambda x: x[1::-1]):
    a = min(W[f:t]+[a])
    if not a:
        continue
    A += a
    for i in range(f, t):
        W[i] -= a
print(A)
