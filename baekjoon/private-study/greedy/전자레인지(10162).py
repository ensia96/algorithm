t = int(input())
A = []
for i in [300, 60, 10]:
    x, y = divmod(t, i)
    A += x,
    t = y
if t:
    print(-1)
else:
    print(*A)
