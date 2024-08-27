T = "bdiopqvwx"
D = {"b": "d", "d": "b", "p": "q", "q": "p"}
while (i := input()) != "#":
    print([i[::-1].translate(str.maketrans(D)), "INVALID"][len({*i} - {*T}) > 0])
