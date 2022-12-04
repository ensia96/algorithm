a, t = 0, 65
for i in map(ord, input()):
    x = abs(t-i)
    a += min(26-x, x)
    t = i
print(a)
