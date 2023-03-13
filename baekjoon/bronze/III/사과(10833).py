A = 0
for _ in ' '*int(input()):
    a, b = map(int, input().split())
    A += b % a
print(A)
