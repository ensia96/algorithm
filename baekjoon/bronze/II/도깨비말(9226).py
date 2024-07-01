while (l := input()) != "#":
    for i in range(len(l)):
        if l[i] in "aiueo":
            l = l[i:] + l[:i]
            break
    print(l + "ay")
