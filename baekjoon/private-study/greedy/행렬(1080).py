I, R = input, range
n, m = map(int, I().split())
A = [[*map(int, I())]for _ in ' '*n]
B = [[*map(int, I())]for _ in ' '*n]
c = 0
for i in R(n-2):
    for j in R(m-2):
        if A[i][j]-B[i][j]:
            for k in R(3):
                for l in R(3):
                    A[i+k][j+l] = not A[i+k][j+l]
            c += 1
for i in R(n):
    for j in R(m):
        A[i][j]-B[i][j] and exit(print(-1))
print(c)
