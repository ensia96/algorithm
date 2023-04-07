x, *A, _ = map(float, [*open(0)])
for a in A:
    print(f'{a-x:.2f}')
    x = a
