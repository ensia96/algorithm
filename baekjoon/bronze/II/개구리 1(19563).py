a, b, c = map(int, input().split())
print("YNEOS"[(c - a - b) % 2 :: 2])
