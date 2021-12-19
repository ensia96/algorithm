import sys
I = sys.stdin.readline
N, C = map(int, I().split())
A = sorted(int(I())for _ in ' '*N)
s, e = 0, A[-1]-A[0]
while s < e:
    m, i, c = (s+e+1)//2, 0, 1
    for j in range(1, N):
        if A[j]-A[i] >= m:
            i, c = j, c+1
    if c >= C:
        s = m
    else:
        e = m-1
print(s)
