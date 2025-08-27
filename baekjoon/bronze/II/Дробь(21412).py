g, n = lambda a, b: b * (a == 0) or g(b % a, a), int(input())
print(*[[i, n - i]for i in range(n // 2)if g(i, n - i) == 1][-1])
