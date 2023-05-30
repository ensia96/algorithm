i, I = 60, 3600
for l in [*open(0)][:-1]:
    m, a, b = map(int, l.split())
    x = int(m*I/a-m*I/b)
    print(f"{x//3600}:{x//i%i:02d}:{x%i:02d}")
