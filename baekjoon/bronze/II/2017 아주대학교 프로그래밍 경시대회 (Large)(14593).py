print(
    sorted([*map(int, ("-" + input()).split()), i] for i in range(int(input())))[0][-1]
    + 1
)
