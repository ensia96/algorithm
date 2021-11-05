t = 0
while 1:
    n, t = int(input()), t+1
    if not n:
        exit()
    b = [[*map(int, input().split())]for _ in range(n)]
    b[0] = [10**9, b[0][1], b[0][1]+b[0][2]]
    for i in range(1, n):
        x, y, z = b[i-1]
        b[i][0] += min(x, y)
        b[i][1] += min(b[i][0], x, y, z)
        b[i][2] += min(b[i][1], y, z)
    print(f"{t}. {b[n-1][1]}")
