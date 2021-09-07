import bisect as b
i = input
l, c = lambda: sorted([*map(int, i().split())]), b.bisect_left

for _ in range(int(i())):
    _, a, b = i(), l(), l()
    print(sum(c(b, i) for i in a))
