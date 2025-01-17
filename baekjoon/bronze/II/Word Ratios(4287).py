for l in [*open(0)][:-1]:
    a, b, c = l.split()
    print(
        a,
        b,
        c,
        "".join(
            chr((ord(c[i]) + ord(b[i]) - ord(a[i]) - 97) % 26 + 97)
            for i in range(len(a))
        ),
    )
