x, y = 1000-int(input()), 0
for i in [500, 100, 50, 10, 5, 1]:
    a, b = divmod(x, i)
    x, y = b, y+a
print(y)
