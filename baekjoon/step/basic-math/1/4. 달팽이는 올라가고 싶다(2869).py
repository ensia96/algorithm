a, b, v = map(int, input().split())

print(round(((v - a) / (a - b)) + 0.4) + 1)
