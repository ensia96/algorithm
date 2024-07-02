f, s, n = (
    lambda x: str((x or "No more")) + " bottle" + "s" * (x != 1) + " of beer",
    "on the wall",
    int(input()),
)
t = f(n)
for i in range(n + 1):
    print(t, s + ",", t.lower() + ".")
    t = f([n - i - 1, n][i == n])
    print(
        ["Take one down and pass it around,", "Go to the store and buy some more,"][
            i == n
        ],
        t.lower(),
        s + ".",
    )
