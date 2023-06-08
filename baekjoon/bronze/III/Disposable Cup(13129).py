a, b, n = map(int, input().split())
x = a*n
A = []
for i in range(n):
    x += b
    A += x,
print(*A)
