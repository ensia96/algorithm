for i in range(1000, 10000):
    t = []
    for j in [10, 12, 16]:
        t += 0,
        x = i
        while x:
            t[-1] += x % j
            x //= j
    if len({*t}) < 2:
        print(i)
