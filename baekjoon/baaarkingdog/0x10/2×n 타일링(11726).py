n, d = int(input()), (1, 2)
for _ in range(2, n):
    d = (d[1], sum(d))
print(d[[1, 0][n == 1]])
