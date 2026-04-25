for l in [*open(0)][1:]:
    i, *I = [["-", chr(i | 32)][0 <= (i | 32) - 97 < 26]
             for i in map(int, l.split())]
    print(*I, i, "ay", sep="")
