a, b, S = map(int, input().split())
l = (a + b + ((a - b)**2 + 4 * S)**.5) / 2
M = int(l)
print(-(M != l) or M)
