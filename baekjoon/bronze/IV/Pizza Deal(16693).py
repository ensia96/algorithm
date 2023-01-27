import math
a, b = map(int, input().split())
x, y = map(int, input().split())
print(a/b > x*x*math.pi/y)
