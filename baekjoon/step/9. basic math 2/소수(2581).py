a = list(
    filter(
        lambda x: x > 1,
        (
            i if all(i % x for x in range(2, i)) else 0
            for i in range(int(input()), int(input()) + 1)
        ),
    )
)

if a:
    print(sum(a))
    print(a[0])
else:
    print(-1)
