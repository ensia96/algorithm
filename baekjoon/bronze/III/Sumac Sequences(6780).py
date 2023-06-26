a, b = map(int, open(0).read().split())
c = 2
while a >= b:
    a, b = b, a-b
    c += 1
print(c)
