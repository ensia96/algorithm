n = int(input())
a = [*map(int, input().split())]
d = [[0]*n for _ in range(n)]
for i in range(n):
    d[i][i], v = 1, a[i]
    for j in range(i+1, n):
        b = v < a[j]
        v, d[i][j] = [v, a[j]][b], d[i][j-1]+b
print(max(map(max, d)))
