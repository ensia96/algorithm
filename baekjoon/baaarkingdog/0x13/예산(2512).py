N = int(input())
A = [*map(int, input().split())]
M = int(input())
s, e = 1, M
while s < e:
    m = (s+e+1)//2
    if sum(min(A[i], m)for i in range(N)) > M:
        e = m-1
    else:
        s = m
print(max(A)if s == M else s)
