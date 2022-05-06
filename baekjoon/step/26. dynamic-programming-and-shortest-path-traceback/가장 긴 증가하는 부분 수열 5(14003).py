import bisect as B
n = int(input())
A = [*map(int, input().split())]
D, T, P, I = [], [], [], []
for i in range(n):
    a = A[i]
    t = B.bisect_left(T, a)
    if t == len(T):
        T += a,
        I += i,
    T[t], I[t] = a, i
    P += [I[t-1], i][not t],
T, x = [], I[-1]
while P[x] != x:
    T += A[x],
    x = P[x]
T += A[x],
print(len(T))
print(*T[::-1])
