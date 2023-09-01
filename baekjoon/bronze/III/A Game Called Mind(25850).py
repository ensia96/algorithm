D, d = [0]*100, 65
for l in [*open(0)][1:]:
    n, *A = map(int, l.split())
    for a in A:
        D[a] = d
    d += 1
print(''.join(chr(D[i])for i in range(100)if D[i]))
