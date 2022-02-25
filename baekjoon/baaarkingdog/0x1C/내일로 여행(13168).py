T = ['Subway', 'Bus', 'Taxi', 'Airplane', 'KTX', 'S-Train',
     'V-Train', 'ITX-Saemaeul', 'ITX-Cheongchun', 'Mugunghwa']
L, M = lambda: map(int, input().split()), 8**8
n, r = L()
C = {t: i for i, t in enumerate(T)}
for i, t in enumerate({*input().split()}):
    C[i], C[t] = t, i
N = range(n)
input()
G = [C[c]for c in input().split()][::-1]
D = [[[[M]*10 for _ in N]for _ in N]for _ in '  ']
for _ in ' '*next(L()):
    t, s, e, c = input().split()
    t, s, e, c = C[t], C[s], C[e], int(c)
    D[0][s][e][t] = D[0][e][s][t] = c
    D[1][s][e][t] = D[1][e][s][t] = c*(1 if t < 5 else 0 if t >= 7 else 0.5)
for i in N:
    for j in N:
        D[0][i][j], D[1][i][j] = min(D[0][i][j]), min(D[1][i][j])
for k in N:
    for i in N:
        for j in N:
            D[0][i][j], D[1][i][j] = min(
                D[0][i][j], D[0][i][k]+D[0][k][j]), min(D[1][i][j], D[1][i][k]+D[1][k][j])
A, B = 0, r
s = G.pop()
while G:
    e = G.pop()
    A += D[0][s][e]
    B += D[1][s][e]
    s = e
print('Yes'if A > B else 'No')
