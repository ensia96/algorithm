_, x, y = open(0)
print(*{*map(int, x.split())}-{*map(int, y.split())})
