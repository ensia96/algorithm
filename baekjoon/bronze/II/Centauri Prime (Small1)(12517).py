for l in map(str.strip, [*open((t := 0))][1:]):
    t += 1
    print(
        f"Case #{t}:",
        l,
        "is ruled by",
        [["a king", "a queen"][l[-1] in "aeiou"], "nobody"][l[-1] == "y"] + ".",
    )
