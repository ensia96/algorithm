for l in [*open(0)][1:]:
    a, b = l.split()
    b = int(b)
    print(f"Shifting {a} by {b} positions gives us:", a[-b:]+a[:-b])
