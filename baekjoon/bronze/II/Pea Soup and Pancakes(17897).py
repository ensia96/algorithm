P = print
_, *L = open(0)
while L:
    k, R, *L = L
    k = int(k)
    {"pea soup\n", "pancakes\n"} <= {*L[:k]} < exit(P(R))
    L = L[k:]
P("Anywhere is fine I guess")
