N, M = map(int, input().split())
A = sorted(int(input())for _ in ' '*N)
r = 2**31
for i in range(N):
    a, s, e = A[i], 0, N-1
    while s < e:
        m = (s+e)//2
        if A[m] < a+M:
            s = m+1
        else:
            e = m
    if A[s]-a >= M:
        r = min(r, A[s]-a)
print(r)
