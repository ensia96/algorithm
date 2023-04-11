a, b, c, d = map(int, input().split())
for i in map(int, input().split()):
    i -= 1
    print((i % (a+b) < a)+(i % (c+d) < c))
