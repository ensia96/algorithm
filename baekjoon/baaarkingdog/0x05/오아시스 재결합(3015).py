A = 0
S = []
for _ in ' '*int(input()):
    h, c = int(input()), 1
    while S and S[-1][0] <= h:
        a, b = S.pop()
        c = b*(a == h)+1
        A += b
    A += bool(S)
    S += (h, c),
print(A)
