import bisect
n = int(input())
A = [*map(int, input().split())]
D = []
for a in A:
    t = bisect.bisect_left(D, a)
    if t == len(D):
        D += a,
    D[t] = a
print(n-len(D))
