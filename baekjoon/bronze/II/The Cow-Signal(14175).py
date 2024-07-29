_, *L = open(0)
_, _, n = map(int, _.split())
for l in L:
    for _ in " " * n:
        print("".join(i * n for i in l[:-1]))
