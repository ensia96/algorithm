I, R, L = input, range, lambda x, y: (y > 0 and x & 1 << y-1)+(x & 1 << y+1)
for _ in ' '*int(I()):
    n, m = map(int, I().split())
    N, M = R(n), 2**m
    A, D = [I()for _ in N], [0]*M
    for i in N:
        d = [-1]*M
        for j in R(M):
            for k in R(M):
                if not D[k]+1:
                    continue
                c = 0
                for x in R(m):
                    if j & 1 << x:
                        if(A[i][x] == 'x')+L(j, x)+L(k, x):
                            break
                        c += 1
                else:
                    d[j] = max(d[j], D[k]+c)
        D = d
    print(max(D))
