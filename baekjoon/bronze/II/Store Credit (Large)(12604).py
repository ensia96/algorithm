_, *A = open(t := 0)
for a, b in zip(map(int, A[::3]), A[2::3]):
    t += 1
    B = [*map(int, b.split())]
    for i in range(len(B)):
        for j in range(i+1, len(B)):
            a == B[i]+B[j] and print(f'Case #{t}:', i+1, j+1)
