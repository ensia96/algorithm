a, b, c, d, e = map(int, input().split())
print(len({*range(a, b+1)} & {*range(c, d+1)}-{e}))
