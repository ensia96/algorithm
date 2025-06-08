input()
A = sorted(map(int, input().split()))
t = len(A)
x = y = z = 0
for a in A:
    if t % 2:
        y += a
    else:
        x += a
    t -= 1
    if x < y:
        z = 1
print(['Alice', 'Bob'][z or y == x])
