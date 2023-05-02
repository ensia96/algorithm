a, b, c = map(int, input().split())
M = 0
for _ in ' '*int(input()):
    A = 0
    for _ in '   ':
        x, y, z = map(int, input().split())
        A += a*x+b*y+c*z
    M = max(M, A)
print(M)
