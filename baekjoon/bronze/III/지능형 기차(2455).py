a = b = 0
while 1:
    x, y = map(int, input().split())
    y or exit(print(b))
    a = a-x+y
    b = max(a, b)
