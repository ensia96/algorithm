n, m, M, t, r = map(int, input().split())
x = y = 0
z = m
while x < n:
    if m+t > M:
        y = -1
        break
    if z+t <= M:
        x += 1
        z += t
    else:
        z = max(m, z-r)
    y += 1
print(y)
