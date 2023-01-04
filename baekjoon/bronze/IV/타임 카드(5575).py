for _ in '   ':
    a, b, c, d, e, f = map(int, input().split())
    _, c = divmod(f-c, 60)
    _, b = divmod(e-b+_, 60)
    _, a = divmod(d-a+_, 24)
    print(a, b, c)
