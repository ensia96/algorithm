for l in [*open(0)][:-1]:
    a, b, c = map(int, l.split())
    x = a//2+1
    print(+(x > b) and (-(x-b > a-b-c) or x-b))
