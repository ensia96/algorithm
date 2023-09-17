input()
x = y = 0
for i in [*map(int, input().split()), 0]:
    if i:
        y += 1
    else:
        x = max(x, y)
        y = 0
print(x)
