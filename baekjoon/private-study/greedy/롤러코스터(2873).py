r, c = map(int, input().split())
A = [[*map(int, input().split())]for _ in ' '*r]
t, x, y = '', r % 2, c % 2
if x+y:
    f = x-y*2
    t = ''.join(['DU', 'RL'][f][i % 2]*~-[r, c][f]+'RD'[f]
                for i in range([c, r][f]-1))+'DR'[f]*~-[r, c][f]
else:
    M, x, y = min((A[i][j], i, j)for i in range(r)for j in range(c)if(i+j) % 2)
    i = p = 0
    while i < r:
        t += 'D'*(i > 0)
        if i in [x-1, x]:
            f, p = 0, 1
            for j in range(c):
                t += 'R'*(j > 0)
                if j-y:
                    t += 'DU'[f]
                    f = not f
        else:
            t += 'RL'[p]*~-c+'D'+'LR'[p]*~-c
        i += 2
print(t)
