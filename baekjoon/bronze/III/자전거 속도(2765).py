i = 0
for l in [*open(0)][:-1]:
    i += 1
    a, b, c = map(float, l.split())
    x = a*3.1415927*b/63360
    print(f"Trip #{i}: {x:.2f} {x/c*3600:.2f}")
