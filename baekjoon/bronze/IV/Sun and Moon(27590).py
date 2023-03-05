a, b = map(int, input().split())
x, y = map(int, input().split())
while a != x:
    if a > x:
        a -= b
    else:
        x -= y
print(-a)
