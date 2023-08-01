n, A = 100-int(input()), []
for i in [25, 10, 5, 1]:
    x, n = divmod(n, i)
    A += x,
print(*A)
