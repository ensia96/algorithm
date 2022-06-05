n = int(input())
A = [*map(int, input().split())]+[0]
m = int(input())
for i in range(n):
    A[i] += A[i-1]
D = [0]*n
for i in range(3):
    d = [0]*n
    for j in range(m*i, n):
        d[j] = max(d[j-1], D[j-m]+A[j]-A[j-m])
    D = d
print(D[-1])
