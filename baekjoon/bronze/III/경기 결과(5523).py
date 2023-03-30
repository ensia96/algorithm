import sys
a = b = 0
for _ in ' '*int(input()):
    x, y = map(int, sys.stdin.readline().split())
    a += x > y
    b += x < y
print(a, b)
