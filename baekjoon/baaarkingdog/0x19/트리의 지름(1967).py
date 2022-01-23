n = int(input())
A, D = 0, [0]*-~n
for p, c, w in [(*map(int, input().split()),)for _ in ' '*~-n][::-1]:
    x, y = D[p], D[c]+w
    A, D[p] = max(A, x+y), max(x, y)
print(A)
