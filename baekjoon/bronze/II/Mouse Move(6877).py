c, r, *L, x, y = map(int, open(0).read().split())
while L:
    i, j, *L = L
    print(x := max(0, min(x + i, c)), y := max(0, min(y + j, r)))
