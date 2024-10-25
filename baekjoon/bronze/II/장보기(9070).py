f = lambda: [*map(int, input().split())]
for _ in " " * f()[0]:
    T = []
    for _ in " " * f()[0]:
        w, c = f()
        T += ([c / w, c, w],)
    print(min(T)[1])
