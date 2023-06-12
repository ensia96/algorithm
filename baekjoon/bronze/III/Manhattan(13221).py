x, y = map(int, input().split())
A, B = 200, (x, y)
for _ in ' '*int(input()):
    a, b = map(int, input().split())
    d = abs(x-a)+abs(y-b)
    if A > d:
        A, B = d, (a, b)
print(*B)
