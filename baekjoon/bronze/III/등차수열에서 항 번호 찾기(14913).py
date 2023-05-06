a, d, k = map(int, input().split())
x, y = divmod((k-a), d)
print([x+1, 'X'][x*d+y != k])
