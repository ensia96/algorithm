a, b, c = map(int, input().split())
for _ in " " * c:
    a ^= b
print(a)
