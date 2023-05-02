a, b = map(int, input().split())
i = 1-2*(b < 0)
x, y = divmod(a, b*i)
print(x*i, y)
