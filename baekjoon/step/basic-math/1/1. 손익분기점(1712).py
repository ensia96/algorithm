a, b, c = map(int, input().split())
x = a // (c - b) + 1

if b > c:
    x = -1

print(x)
