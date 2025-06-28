for l in [*open(0)][:-1]:
    a, b, c, d = map(int, l.split())
    print(1080+((a-b+40) % 40+(c-b+40) % 40+(c-d+40) % 40)*9)
