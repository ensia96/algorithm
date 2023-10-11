n = int(input())
a = b = c = 0
while n:
    x = n//2
    a, b = [(a, b+n-x), (a+n-x, b)][c]
    n = x
    c = not c
print(a, b)
