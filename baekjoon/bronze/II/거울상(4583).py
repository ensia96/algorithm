D = {"b": "d", "d": "b", "p": "q", "q": "p"}
while (i := input()) != "#":
    r = i[::-1].translate(str.maketrans(D))
    print([r, "INVALID"][i == r])
