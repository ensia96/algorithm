A = []
for _ in ' '*int(input()):
    a, b = map(int, input().split())
    if b >= a:
        A += b,
print(min(A)if A else -1)
