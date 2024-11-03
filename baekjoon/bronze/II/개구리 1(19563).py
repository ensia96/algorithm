a, b, c = map(abs, map(int, input().split()))
print("YNEOS"[(c < a + b) or (c - a - b) % 2 :: 2])
