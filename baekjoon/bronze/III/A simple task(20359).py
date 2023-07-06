n = int(input())
for i in range(6, 0, -1):
    x, y = divmod(n, 2**i)
    y or exit(print(x, i))
