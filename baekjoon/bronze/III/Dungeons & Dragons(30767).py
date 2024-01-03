a, b, c, d, e = map(int, open(0).read().split())
print(max(0, min(a-b, e)-max(a-c, d)+1))
