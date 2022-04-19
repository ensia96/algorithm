import bisect as B
n = int(input())
A, D = [*map(int, input().split())][::-1], [0]
for a in A:
    t = B.bisect_left(D, a)
    D += [] if t-len(D)else [a]
    D[t] = min(D[t], a)
print(len(D) - 1)
