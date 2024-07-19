n, *A = map(int, open(0).read().split())
print(
    ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"][
        A.index(max(A)) // n
    ]
)
