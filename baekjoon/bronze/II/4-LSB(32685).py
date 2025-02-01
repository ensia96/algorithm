print(
    str(
        int(
            "".join(
                bin(i)[2:][-4:].rjust(4, "0") for i in map(int, open(0).read().split())
            ),
            2,
        )
    ).rjust(4, "0")
)
