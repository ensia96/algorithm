n, t, c, p = map(int, input().split())
print(sum(c for i in range(1, n)if not i % t)*p)
