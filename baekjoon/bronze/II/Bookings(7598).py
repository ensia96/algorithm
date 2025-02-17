while (s := input().split())[0] != "#":
    a, b = s
    b = int(b)
    while (s := input().split())[0] != "X":
        c, d = s
        d = int(d)
        b = [[b, b - d][b >= d], [b, b + d][b + d < 69]][c == "B"]
    print(a, b)
