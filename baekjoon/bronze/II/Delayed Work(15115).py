k, p, x = map(int, input().split())
y = 1e9
for i in range(1, 9999):
    y = min(y, k * p / i + x * i)
print(f"{y:.3f}")
