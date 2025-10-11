a, b, c, *T = map(lambda x: int((float(x) + 0.005) * 100), input().split())
for i in range(0, a + 1, b):
    if not (a - i) % c:
        T += (i // b, (a - i) // c),
for t in T or [('none')]:
    print(*t)
