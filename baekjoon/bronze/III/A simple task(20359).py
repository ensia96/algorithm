n = int(input())
for i in range(6):
    x, y = divmod(n, 2**i)
    x % 2 and (y or exit(print(x, i)))
