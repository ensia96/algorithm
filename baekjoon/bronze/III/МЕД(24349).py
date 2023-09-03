n, a, b, c = map(int, input().split())
t = min(a, b)
print(*divmod(n > 1 and [t+(n-2)*c, t*~-n][a < c or b < c], 100))
