x = 1
for l in [*open(0)][1:]:
    a, b = map(int, l.split())
    print(f'Case #{x}:', sum(a <= i**3 <= b for i in range(1260)))
    x += 1
