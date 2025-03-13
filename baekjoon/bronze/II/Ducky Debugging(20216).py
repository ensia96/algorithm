for l in [*open(0)][::2]:
    print()
    if "I quacked the code!\n" == l:
        exit()
    print("Q*uNaocdk*!"[l[-2] < "?" :: 2])
