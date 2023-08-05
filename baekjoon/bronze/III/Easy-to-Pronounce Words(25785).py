a = b = t = 1
for i in input():
    x = i in 'aeiou'
    y = not x
    a *= [x, y][t % 2]
    b *= [y, x][t % 2]
    t += 1
print(a+b)
