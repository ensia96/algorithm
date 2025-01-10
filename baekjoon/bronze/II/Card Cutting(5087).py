for l in [*open(0)][:-1]:
    print(
        ["Draw", "Tania", "Cheryl"][
            (
                (
                    x := (
                        A := [i % 2 for i in map(int, l[:-2].replace("A", "1").split())]
                    ).count(0)
                )
                > (y := A.count(1))
            )
            + 2 * (y > x)
        ]
    )
