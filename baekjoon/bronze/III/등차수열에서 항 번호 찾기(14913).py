a, d, k = map(int, input().split())
x, y = divmod((k-a), d)
print([x+1, 'X'][y > 0 or k < a])
