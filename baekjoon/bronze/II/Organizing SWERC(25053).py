for _ in ' '*int(input()):
    t = [0]*10
    for _ in ' '*int(input()):
        b, d = map(int, input().split())
        t[d-1] = max(t[d-1], b)
    print([sum(t), "MOREPROBLEMS"][min(t) < 1])
