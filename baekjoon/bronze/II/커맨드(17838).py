for l in [*open(0)][1:]:
    print(
        +(
            2 == len({*l.strip()})
            and l.replace(l[0], "A").replace(l[2], "B") == "AABBABB\n"
        )
    )
