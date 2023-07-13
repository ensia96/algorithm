a, b, c = map(int, input().split())
x = 0
while a >= 0:
    a -= [b, c][x]
    x = not x
print(+x)
