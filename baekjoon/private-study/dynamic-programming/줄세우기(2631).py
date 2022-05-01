import bisect as B
n = int(input())
A = [int(input())for _ in ' '*n]
T = []
for a in A:
    t = B.bisect_left(T, a)
    if t == len(T):
        T += a,
    T[t] = min(T[t], a)
print(n-len(T))
