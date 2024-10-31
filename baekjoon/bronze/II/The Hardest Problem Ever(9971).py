for l in [*open(0)][1:-1:3]:
    print(
        "".join([[i, chr((x := ord(i) - 5) + 26 * (x < 65))][i.isalpha()] for i in l])[
            :-1
        ]
    )
