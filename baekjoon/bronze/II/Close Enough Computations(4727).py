while 0 < sum(A := [*map(int, input().split())]):
    C, f, c, p = A
    print('yneos'[(9 * max(f - .5, 0) + 4 * max(c - .5, 0) + 4 *
          max(p - .5, 0)) > C < 9 * (f + .5) + 4 * (c + p + 1)::2])
