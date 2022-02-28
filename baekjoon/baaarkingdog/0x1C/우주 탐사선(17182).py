L, A = lambda: map(int, input().split()), 4**7
N, K = L()
n = range(N)
T = [[*L()]for _ in n]
for k in n:
    for i in n:
        for j in n:
            T[i][j] = min(T[i][j], T[i][k]+T[k][j])
V = [0]*N
V[K] = 1


def F(i, s, R):
    global A
    if all(V):
        A = min(A, s)
        return
    for j in n:
        if V[j]:
            continue
        V[j] = 1
        F(j, s+T[i][j], R+[j])
        V[j] = 0


F(K, 0, [K])
print(A)
