for _ in range(int(input())):
    n = int(input())
    d = [(1, 0), (0, 1)]+[0]*(n-1)
    for i in range(2, n+1):
        a, b = d[i-1], d[i-2]
        d[i] = (a[0]+b[0], a[1]+b[1])
    print(*d[n])
