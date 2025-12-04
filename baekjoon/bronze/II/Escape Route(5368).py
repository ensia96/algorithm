I = input
for _ in '_' * int(I()):
    N = range(int(I()))
    M = [I()for _ in N]
    a, b = min((y, x)for y in N if (x := M[y].find('s')) > -1)
    c, d, e = min([((y - a)**2 + (x - b)**2, y, x)
                  for y in N if (x := M[y].find('p')) > -1])
    print(f"({a},{b}):({d},{e}):{c**0.5:.2f}")
