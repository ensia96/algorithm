t, p = map(int, input().split())
print(t / (max(0, 20 - p) * 2 + min(80, 100 - p)) * (max(0, p - 20) + 2 * min(20, p)))
