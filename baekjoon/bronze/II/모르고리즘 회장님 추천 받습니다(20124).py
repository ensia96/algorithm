print(
    sorted([l.split() for l in [*open(0)][1:]], key=lambda x: (-int(x[1]), x[0]))[0][0]
)
