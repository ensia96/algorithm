import sys
i = sys.stdin.readline
for _ in range(int(i())):
    _, a, m = i(), 0, 0
    for p in [*map(int, i().split())][::-1]:
        a, m = [(a+m-p, m), (a, p)][p > m]
    print(a)
