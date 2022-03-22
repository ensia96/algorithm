def check(w):
    d, c = {0}, w[0]
    for i in w:
        if i != c:
            c = i
            if i in d:
                return 0
        d.add(i)
    return 1


print(sum(map(check, [*open(0)][1:])))
