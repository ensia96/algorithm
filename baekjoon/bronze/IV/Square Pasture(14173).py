a, b, c, d = map(int, input().split())
h, i, j, k = map(int, input().split())
print(max(max(c, j)-min(a, h), max(d, k)-min(b, i))**2)
