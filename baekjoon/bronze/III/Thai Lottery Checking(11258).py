*X, _ = open(0).read().split()
a, A, b, B, c, C, d, D, e, E, f, F, *X = X
for x in X:
    print((a == x)*int(A)+(b == x[:3])*int(B)+(c == x[:3])*int(C) +
          (d == x[3:])*int(D)+(e == x[3:])*int(E)+(f == x[4:])*int(F))
