*A, = map(int, open(0))
x = y = 0
while A:
    a = A.pop()
    if x < a:
        y += 1
        x = a
print(y)
