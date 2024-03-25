for l in open(0):
    n, k = map(int, l.split())
    x = n
    while n >= k:
        x += n//k
        n = n-n//k*k+n//k
    print(x)
