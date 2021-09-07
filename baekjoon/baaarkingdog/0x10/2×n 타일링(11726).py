n, d = int(input()), (1, 2)
for _ in range(2, n):
    d = (d[1], sum(d))
print(d[not n == 1] % 10007)
