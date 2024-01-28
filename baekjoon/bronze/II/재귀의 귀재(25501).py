for l in [*open(0)][1:]:
    i, t = 0, ~len(l)//-2
    while i < t and l[i] == l[-i-2]:
        i += 1
    print(+(i == t), i+(i != t))
