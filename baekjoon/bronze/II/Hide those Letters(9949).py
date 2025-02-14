while (A := input()) != "# #":
    a, b = A.split()
    for _ in " " * int(input()):
        print(
            input()
            .replace(a, "_")
            .replace(a.upper(), "_")
            .replace(b, "_")
            .replace(b.upper(), "_")
        )
