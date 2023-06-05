while 1:
    n = int(input())
    if n == -1:
        break
    x = y = 0
    for i in ' '*n:
        s, t = map(int, input().split())
        y += s*(t-x)
        x = t
    print(y, 'miles')
