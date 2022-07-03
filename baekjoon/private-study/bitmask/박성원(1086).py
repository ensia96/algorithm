n = int(input())
M = 1 << n
A = [input()for _ in ' '*n]
k = int(input())
D = [k*[-1]for _ in ' '*M]
R = [k*[-1]for _ in ' '*n]
F, G = lambda x: +(x < 2) or x*F(x-1), lambda x, y: y == 0 and x or G(y, x % y)


def f(x, y):
    if x == M-1:
        D[x][y] = +(not y)
    elif D[x][y] == -1:
        D[x][y] = 0
        for i in range(n):
            if not x & 1 << i:
                if R[i][y] == -1:
                    R[i][y] = int(str(y)+A[i]) % k
                D[x][y] += f(x | 1 << i, R[i][y])
    return D[x][y]


a, b = f(0, 0), F(n)
c = G(a, b)
print(f"{a//c}/{b//c}")
