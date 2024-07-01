for l in [*open(0)][:-1]:
    for i in range(len(l)):
        if l[i] in "aiueo\n":
            print(l[i:-1] + l[:i] + "ay")
            break
