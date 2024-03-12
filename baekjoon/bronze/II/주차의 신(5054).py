f, r = lambda: map(int, input().split()), range
for _ in r(*f()):
    f()
    A = *f(),
    print((max(A)-min(A))*2)
