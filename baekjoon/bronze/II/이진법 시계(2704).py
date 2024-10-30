f = lambda x: f"{int(bin(x)[2:]):06d}"
for l in [*open(0)][1:]:
    h, m, s = map(int, l.split(":"))
    T = f(h) + f(m) + f(s)
    print("".join(T[i] + T[6 + i] + T[12 + i] for i in range(6)), T)
