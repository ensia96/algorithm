for l in [*open(0)][:-1]:
    a, b, c, *A = map(float, l.split())
    if b >= 150 and c >= 200 and a <= 4.5:
        A += 'Wide Receiver',
    if b >= 300 and c >= 500 and a <= 6:
        A += 'Lineman',
    if b >= 200 and c >= 300 and a <= 5:
        A += 'Quarterback',
    print(*A or ['No', 'positions'])
