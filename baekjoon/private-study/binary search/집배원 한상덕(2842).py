import bisect
n = int(input())
N = range(n)
A = [input()for _ in N]
C = [[*map(int, input().split())]for _ in N]
S = set()
h = l = r = 0
for i in N:
    for j in N:
        if A[i][j] == 'P':
            x, y = i, j
        if A[i][j] == 'K':
            h += 1
        S.add(C[i][j])
S = sorted(S)
L = len(S)
M = 8**7
while l <= r < L:
    Q, V = [(x, y)], [n*[1]for _ in N]
    V[x][y] = c = 0
    if S[l] <= C[x][y] <= S[r]:
        while Q:
            i, j = Q.pop()
            for p, q in [(i+1, j+1), (i+1, j), (i+1, j-1), (i, j+1), (i, j-1), (i-1, j+1), (i-1, j), (i-1, j-1)]:
                if 0 <= p < n > q >= 0 and V[p][q] and S[l] <= C[p][q] <= S[r]:
                    V[p][q] = 0
                    c += A[p][q] == 'K'
                    Q += (p, q),
    if c == h:
        M = min(M, S[r]-S[l])
        l += 1
    else:
        r += 1
print(M)
