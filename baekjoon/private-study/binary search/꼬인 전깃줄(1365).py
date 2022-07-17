import bisect
n = int(input())
D = []
for a in map(int, input().split()):
    t = bisect.bisect_left(D, a)
    if t == len(D):
        D += a,
    D[t] = a
print(n-len(D))
