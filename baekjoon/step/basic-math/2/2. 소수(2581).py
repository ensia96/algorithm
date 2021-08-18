a = list(
    filter(
        bool,
        (
            i if all(i % x for x in range(2, i)) else 0
            for i in range(int(input()), int(input()) + 1)
        ),
    )
)

if a:
    print(sum(a))
    print(min(a))
else:
    print(-1)
