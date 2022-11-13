n, m = map(int, input().split())
T = []
c = 0
for _ in ' '*n:
    p, l = map(int, input().split())
    A = sorted(map(int, input().split()))
    T += 1 if l > p else A[-l],
for t in sorted(T):
    if m >= t:
        m -= t
        c += 1
print(c)
