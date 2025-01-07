for l in [*open(0)][1:]:
    print(sum((i in "ABDOPQR") + (i == "B") for i in l))
