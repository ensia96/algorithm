S = "\\!#$%&'()-0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_`{}~"
D = {S[i]: i for i in range(53)}
n = int(input())
M = 80*n+1
C = [0]*M
N = [53*[-1]for _ in ' '*M]
U = 1
for _ in ' '*n:
    c = 0
    for s in input():
        t = D[s]
        if N[c][t] == -1:
            N[c][t] = U
            U += 1
        if t == 0:
            C[c] = 1
        c = N[c][t]
    C[c] = 1


def f(x, y, z):
    C[x] and print(' '*y+z)
    for i in range(53):
        0 < N[x][i] and f(N[x][i], y+(not i), z+S[i]if i else'')


f(0, 0, '')
