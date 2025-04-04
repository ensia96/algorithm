for l in [*open(0)][1:]:
    print(
        "".join(
            "abcdefghijklmnopqrstuvwxyz "[(sum(map(ord, i)) - len(i) * 97) % 27]
            for i in l.split()
        )
    )
