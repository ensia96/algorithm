i = 0
while (A := input()) != "# #":
    print("Case", i := i + 1)
    a, b = A.split()
    for _ in " " * int(input()):
        print(
            input()
            .replace(a, "_")
            .replace(a.upper(), "_")
            .replace(b, "_")
            .replace(b.upper(), "_")
        )
    print()
