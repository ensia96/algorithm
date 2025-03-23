for l in [*open(0)][1:]:
    print(
        "The number of vowels in",
        l.strip(),
        "is",
        str(sum(l.count(c) for c in "aeiou")) + ".",
    )
