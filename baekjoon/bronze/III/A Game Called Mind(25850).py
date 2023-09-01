D, d = [0]*100, 65
for _ in ' '*int(input()):
    n, *A = map(int, input().split())
    for a in A:
        D[a] = d
    d += 1
print(''.join(chr(D[i])for i in range(100)if D[i]))
