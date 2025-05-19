for i in [*open(x := 0)][1].split():
    t = i[-1] in '.?!'
    x += i[0].isupper()*all(map(str.islower, [i[1:], i[1:-1]][t]))
    if t:
        print(x)
        x = 0
