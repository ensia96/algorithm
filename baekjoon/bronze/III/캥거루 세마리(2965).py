a, b, c = map(int, input().split())
A = -1
while a < b < c:
    A += 1
    x = b-a < c-b
    a, b, c = [(a, a+1, b), (b, b+1, c)][x]
print(A)
