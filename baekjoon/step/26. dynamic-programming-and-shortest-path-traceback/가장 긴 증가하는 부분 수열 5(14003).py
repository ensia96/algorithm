import bisect as B
n = int(input())
A = [*map(int, input().split())]
T, P = [], []
for i in range(n):
    a = A[i]
    t = B.bisect_left(T, (a, 0))
    if t == len(T):
        T += (a, i),
    T[t] = (a, i)
    P += [T[t-1][1], i][not t],
T, x = [], T[-1][1]
while P[x] != x:
    T += A[x],
    x = P[x]
T += A[x],
print(len(T))
print(*T[::-1])
