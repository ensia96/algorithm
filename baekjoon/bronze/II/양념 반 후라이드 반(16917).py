a, b, c, x, y = map(int, input().split())
m, M = min(x, y), max(x, y)
print(min(m*min(a+b, c*2)+[a, b][M == y]*(M-m), M*2*c, a*x+b*y))
