p, t = 3.14159, 0
for l in [*open(0)][1:]:
    a, *A = l.split()
    r = float(A[0])
    t = max(t, p*(3+(a == 'S')-2*(a == 'C'))*r *
            r*(r if a == 'S'else float(A[1]))/3)
print(t)
