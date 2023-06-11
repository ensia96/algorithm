n, w, h, *A = map(int, open(0).read().split())
for a in A:
    print('YNEOS'[w*w+h*h < a*a::2])
