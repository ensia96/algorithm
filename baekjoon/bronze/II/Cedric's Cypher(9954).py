for l in [*open(0)][:-1]:
    x = ord(l[-2]) - 65
    print(
        "".join(
            [
                i,
                chr(
                    (ord(i) - x - 65 - 32 * i.islower()) % 26 + 65 + 32 * (i.islower())
                ),
            ][i.isalpha()]
            for i in l[:-2]
        )
    )
