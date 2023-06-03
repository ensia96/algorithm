n, t = map(int, input().split())
x = y = 0
for i in range(t):
    x = [x, 1, 0][(y == 2*n)+2*(y == 1)]
    y += 1-2*x
print(y)
