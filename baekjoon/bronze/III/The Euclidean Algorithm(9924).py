a, b = map(int, input().split())
c = 0
while a > b:
    a, b = b, a-b
    c += 1
print(c)
