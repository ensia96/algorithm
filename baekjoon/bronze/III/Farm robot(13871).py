a, b, c, *L = map(int, open(0).read().split())
x, y = 1, c == 1
for i in L:
    x = (x+i) % a or a
    y += x == c
print(y)
