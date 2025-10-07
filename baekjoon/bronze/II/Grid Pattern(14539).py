i, j, k, l, m = '-|+* '
for L in [*open(T := 0)][1:]:
    T += 1
    r, c, w, h = map(int, L.split())
    print(f'Case #{T}:', a := k + (i * w + k) * c,
          *[((j + w * l) * c + j + m) * h + a] * r)
