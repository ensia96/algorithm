n, o = map(int, open(0))
x, y = divmod(o*n, (n-1))
print(x-(not y), x)
