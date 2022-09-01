M = 360000
n = int(input())
B = [0]*M
A = B+B
for a in map(int, input().split()):
    A[a] = A[a+M] = 1
for b in map(int, input().split()):
    B[b] = 1
f, j = [0]*M, 0
for i in range(1, M):
    while j and B[i] != B[j]:
        j = f[j-1]
    if B[i] == B[j]:
        j += 1
        f[i] = j
j = 0
for i in range(2*M):
    while j and A[i] != B[j]:
        j = f[j-1]
    j += A[i] == B[j]
    if j == M-1:
        exit(print('possible'))
print('impossible')
