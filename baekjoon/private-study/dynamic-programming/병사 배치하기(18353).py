import bisect as B
n = int(input())
A = [*map(int, input().split())]
D = []
for a in A[::-1]:
    t = B.bisect_left(D, a)
    if t == len(D):
        D += a,
    D[t] = a
print(n-len(D))
