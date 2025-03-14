M = "January February March April May June July August September October November December".split()
while (l := input()) != "0 #":
    d, m = l.split()
    m = M.index(m)
    d = int(d)
    print(
        [
            ["YNeos"[7 < m or m == 7 and m > 4 :: 2], "Happy birthday"][
                m == 7 and d == 4
            ],
            "Unlucky",
        ][m == 1 and d == 29]
    )
