while 1:
    n = int(input())
    n > 0 or exit()
    x = y = 0
    for _ in ' '*n:
        s, t = map(int, input().split())
        x += s*(t-y)
        y = t
    print(x, 'miles')
