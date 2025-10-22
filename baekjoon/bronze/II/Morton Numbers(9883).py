x, y = map(bin, map(int, input().split()))
n = max(len(x), len(y)) - 2
print(int(''.join(i + j for i, j in zip(x[2:].zfill(n), y[2:].zfill(n))), 2))
