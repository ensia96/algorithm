H = 100
for l in [*open(0)][1:]:
    a, b, c, d = l.split()
    x = float(a) * (H - 5 * (" WOYB G  R".index(b))) * (H - 5 * (c == "C"))
    print(f"${(x+.5)//(H*(t:=10**(d=='C')))/H*t:.2f}")
