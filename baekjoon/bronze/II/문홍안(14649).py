p, *A = open(0).read().split()
for b in map(
    [
        sum([a < i, i < a][b == "L"] for a, b in zip(map(int, A[1::2]), A[2::2])) % 3
        for i in range(1, 101)
    ].count,
    range(3),
):
    print(f"{int(p)/100*b:.2f}")
