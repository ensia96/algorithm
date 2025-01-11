a, b, k = map(int, input().split())
print((x := a // k) * (y := b // k) - max(0, x - 2) * max(0, y - 2))
