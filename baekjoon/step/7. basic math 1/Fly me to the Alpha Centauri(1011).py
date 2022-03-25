for _ in range(int(input())):
    x, y = map(int, input().split())
    a, i = y - x, 0
    while i * (i + 1) < a:
        i += 1
    i -= 1

    print((i * 2) + 2 if a - (i * (i + 1)) > i + 1 else (i * 2) + 1)
