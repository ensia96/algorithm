for l in [*open(0)][1:]:
    try:
        for i in l:
            if i in "+-":
                raise ValueError
        print(int(l))
    except:
        print("invalid input")
