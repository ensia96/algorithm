r, c, a, b = map(int, open(0).read().split())
for i in range(r):
    for j in range(a):
        print(''.join(b*'X.'[(i % 2) ^ (k % 2)]for k in range(c)))
