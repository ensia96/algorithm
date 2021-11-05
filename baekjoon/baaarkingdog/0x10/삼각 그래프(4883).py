l, t = lambda: [*map(int, input().split())], 0
while 1:
    n, t = int(input()), t+1
    if not n:
        exit()
    a, b, c = l()
    a, c = 10**9, b+c
    for _ in range(n-1):
        x, y, z = l()
        x += min(a, b)
        y += min(x, a, b, c)
        z += min(y, b, c)
        a, b, c = x, y, z
    print(f"{t}. {y}")
