n, x = map(int, input().split())
*A, = map(int, input().split())
i = 1
while A[(i-1) % n] > x+i:
    i += 1
print((i-1) % n or 1)
