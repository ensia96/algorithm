for l in [*open(0)][1:]:
    print(
        +(
            2 == len({*l.strip()})
            and "!!??!??\n" == l.replace(l[0], "!").replace(l[2], "?")
        )
    )
