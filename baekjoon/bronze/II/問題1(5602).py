a = 0
print(
    *map(
        lambda x: x[1],
        sorted(
            [-sum(i), (a := a + 1)]
            for i in zip(*[[*map(int, l.split())] for l in [*open(0)][1:]])
        ),
    )
)
