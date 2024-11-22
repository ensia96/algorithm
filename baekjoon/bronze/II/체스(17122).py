for l in [*open(0)][1:]:
    x, y = l.split()
    p, q = divmod(int(y), 8)
    print(
        "YNEOS"[
            1
            - (
                ((ord(x[0]) % 2) ^ (int(x[1]) % 2)) ^ ((p - (q == 0)) % 2) ^ (q % 2)
            ) :: 2
        ]
    )
