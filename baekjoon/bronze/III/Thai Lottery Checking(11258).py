*X, _ = open(0).read().split()
a, A, b, B, c, C, d, D, e, E, f, F, *X = X
for x in X:
    print(sum((t in x)*int(T)
          for t, T in [(a, A), (b, B), (c, C), (d, D), (e, E), (f, F)]))
