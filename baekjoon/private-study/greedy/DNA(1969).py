n, m = map(int, input().split())
C = [{}for _ in ' '*m]
for _ in ' '*n:
    d = input()
    for i in range(m):
        C[i][d[i]] = C[i].get(d[i], 0)-1
print(''.join(sorted(C[i].items(), key=lambda x: (
    x[1], x[0]))[0][0]for i in range(m)))
