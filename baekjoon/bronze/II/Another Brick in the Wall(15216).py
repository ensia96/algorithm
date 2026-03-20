h, w, _, *A = map(int, open(x := 0).read().split())
while A * h and (x := x + A.pop(0)) <= w:
    h -= x == w
    x %= w
print("YNEOS"[h > 0::2])
