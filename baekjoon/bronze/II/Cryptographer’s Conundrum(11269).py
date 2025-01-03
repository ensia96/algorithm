A = input()
print(
    sum(
        sum([a != "P", b != "E", c != "R"]) for a, b, c in zip(A[::3], A[1::3], A[2::3])
    )
)
