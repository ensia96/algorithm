_, A = open(0)
x, y = 1, 0
for a in A[:-1]:
    if a == 'L':
        x = max(1, x-1)
    if a == 'R':
        x = min(3, x+1)
    y += x == 3
print(y)
