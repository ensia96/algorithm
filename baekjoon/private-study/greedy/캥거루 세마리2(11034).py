for l in open(0):
    a, b, c = map(int, l.split())
    print(max(b-a, c-b)-1)
