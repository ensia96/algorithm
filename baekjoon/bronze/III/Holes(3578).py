n = int(input())
x, y = divmod(n, 2)
print([+(not n), '4'*y+'8'*x][n > 1])
