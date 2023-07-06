n = int(input())
for i in range(7):
    x, y = divmod(n, 2**i)
    y or (x % 2 and exit(print(x, i)))
print(1, i)
