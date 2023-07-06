k, d = map(int, input().split())
x = y = 0
while x+k <= d:
    x += k
    k *= 2
    y += 1
print(y)
