for a in range(1, 10):
    print("? A", a, flush=True)
    if input() > '0':
        for b in range(1, 10):
            print("? B", b, flush=True)
            input() > '0' and exit(print("!", a+b))
