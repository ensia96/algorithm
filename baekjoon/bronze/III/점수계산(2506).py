a, A = open(0)
x = y = 0
for i in map(int, A.split()):
    x = i and x+i
    y += x
print(y)
