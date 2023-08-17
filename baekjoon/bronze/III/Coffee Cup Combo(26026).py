input()
x = y = 0
for a in input():
    t = a > '0'
    y += [x > 0, 1][t]
    x = [[x, x-1][x > 0], 2][t]
print(y)
