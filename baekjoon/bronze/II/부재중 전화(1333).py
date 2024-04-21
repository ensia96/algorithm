n, l, d = map(int, input().split())
l += 5
x = 0
y = d
for i in range(n):
    x += l
    while 1:
        if y < x-5:
            y += d
        else:
            break
    if x-5 <= y < x:
        break
print(y)
