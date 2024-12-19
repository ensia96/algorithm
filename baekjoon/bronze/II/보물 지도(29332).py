M = 1e6
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
print([(L - R - 1) * (D - U - 1), "Infinity"][L == M or D == M or R == -M or U == -M])
