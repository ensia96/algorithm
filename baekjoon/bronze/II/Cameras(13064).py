for l in [*open(0)][1:]:
    l[0] == l[1] and all([l[i].isdigit, l[i].isupper][i == 4]()
                         for i in range(8)) and print(l[:-1])
