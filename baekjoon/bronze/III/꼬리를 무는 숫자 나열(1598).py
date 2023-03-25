n, m = map(int, input().split())
a, b = divmod(n, 4)
x, y = divmod(m, 4)
print(abs(x-a)+abs(b-y))
