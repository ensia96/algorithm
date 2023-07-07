A = [0]*4
for l in [*open(0)][1:]:
    a, b, c = map(int, l.split())
    if a < 2:
        A[3] += 1
    elif b < 3:
        A[0] += 1
    else:
        A[b-2] += 1
for a in A:
    print(a)
