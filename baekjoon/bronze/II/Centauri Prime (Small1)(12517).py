for l in [*open((t := 0))][1:]:
    t += 1
    print(
        f"Case #{t}:",
        l[:-1],
        "is ruled by",
        [["a king", "a queen"][l[-2] in "aeiou"], "nobody"][l[-2] == "y"] + ".",
    )
