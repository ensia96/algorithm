M = 1e10
L = D = M
R = U = -M
for l in [*open(0)][1:]:
    x, y, d = l.split()
    if d == "L":
        L = min(L, int(x))
    if d == "R":
        R = max(R, int(x))
    if d == "U":
        U = max(U, int(y))
    if d == "D":
        D = min(D, int(y))
print([(L - R - 1) * (D - U - 1), "Infinity"][any([L == M, D == M, R == -M, U == -M])])
