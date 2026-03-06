for l in [*open(t := 0)][2::2]:
    *l, = map(int, l.split())
    t += 1
    print(f'Case #{t}:', 'YNEOS'[any(2 * b - a in l[j + 1:]
          for j, b in enumerate(l)for a in l[:j])::2])
