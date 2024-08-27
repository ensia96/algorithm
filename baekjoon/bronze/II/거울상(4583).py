D = {"b": "d", "d": "b", "p": "q", "q": "p"}
for l in [*open(0)][:-1]:
    l = l.strip()
    r = l[::-1].translate(str.maketrans(D))
    print([r, "INVALID"][l == r])
