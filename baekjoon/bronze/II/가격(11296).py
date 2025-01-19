H = 100
for l in [*open(0)][1:]:
    a, b, c, d = l.split()
    print(
        f"${round(float(a)/H*(H-5*(' WOYB G  R'.index(b)))/H*(H-5*(c=='C')),2-(d=='C')):.2f}"
    )
