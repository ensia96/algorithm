print(
    "".join(l[l.lower().index("x") + l.index(" ") + 1].upper() for l in [*open(0)][1:])
)
