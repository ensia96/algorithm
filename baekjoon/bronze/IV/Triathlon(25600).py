A = 0
for _ in ' '*int(input()):
    a, d, g = map(int, input().split())
    A = max(A, (1+(a == d+g))*a*(d+g))
print(A)
