for l in [*open(0)][1:]:
    f = '.' in l
    *A, y = map(int, l[:-1].split('/.'[f]))
    d, m = A[::2 * f - 1]
    print(f'{d:02d}.{m:02d}.{y:04d}', f'{m:02d}/{d:02d}/{y:04d}')
