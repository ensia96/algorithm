import bisect as B
input()
D = []
for a in map(int, input().split()):
    t = B.bisect_left(D, a)
    if t == len(D):
        D += a,
    D[t] = a
print(len(D))
