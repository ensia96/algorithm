n = int(input())
for i in range(6):
    x, y = divmod(n, 2**i)
    y or (x % 2 and exit(print(x, i)))
