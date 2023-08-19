c = 0
for l in [*open(0)][1:]:
    c += 1
    a, b = map(int, l.split())
    print(f'Case {c}:', b-a+1)
