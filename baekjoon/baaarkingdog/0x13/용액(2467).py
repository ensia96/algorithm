import bisect as B
n = int(input())
L = [*map(int, input().split())]
S, P = 2**31, 0
for i in range(n):
    I = B.bisect_left(L, -L[i])
    for j in range(I-1, I+1):
        if (j < 0)+(j >= n)+(i == j):
            continue
        s = abs(L[i]+L[j])
        if S > s:
            S, P = s, (L[i], L[j])
print(*sorted(P))
