n = int(input())
A = [*map(int, input().split())]
D = [0]
d = [0]
for i in range(n):
    D += max(D[-1]+A[i], A[i]),
    d += max(d[-1]+A[-i-1], A[-i-1]),
A = max(D[1:])
for i in range(1, n):
    A = max(A, D[i]+d[-i-2])
print(A)
