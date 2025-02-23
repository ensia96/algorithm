for l in [*open(i := 0)][1:]:
    i += 1
    g, f, m = l.split()
    a, b, c, d = map(int, [*f[:-1].split("'"), *m[:-1].split("'")])
    x = a * 12 + b + c * 12 + d + 5 * (1 - 2 * (g == "G"))
    t = x % 2
    x //= 2
    print(
        f"Case #{i}: {int((x-4+t)//12//1)}'{int((x-4+t)%12//1)}\" to {int((x+4)//12//1)}'{int((x+4)%12//1)}\""
    )
