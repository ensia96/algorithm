_, r, *A = open(t := 0).read().split()
r = int(r)
for a in A:
    d, m = divmod(r - len(a), 2)
    print("." * (d + m * t) + a + "." * (d + m - m * t))
    t ^= m
