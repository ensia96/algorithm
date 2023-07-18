for l in open(0):
    n, w, d, s = map(int, l.split())
    print(((n*~-n//2*w)-s)//d or n)
