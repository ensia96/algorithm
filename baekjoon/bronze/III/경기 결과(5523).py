import sys
a = b = 0
for _ in ' '*int(input()):
    x = map(int, sys.stdin.readline().split())
    a += x > y
    b += x < y
print(a, b)
