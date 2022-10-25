for _ in ' '*int(input()):
    n, m = map(int, input().split())
    t, c = [1]*n, 0
    for a, b in sorted([[*map(int, input().split())]for _ in ' '*m], key=lambda x: x[::-1]):
        for i in range(a-1, b):
            if t[i]:
                t[i] = 0
                c += 1
                break
    print(c)
