for i in [*open(T := 0)][1:]:
    T += 1
    r, c, w, h = map(int, i.split())
    print(f'Case #{T}:', a := '+' + ('-' * w + '+') * c,
          *[(('|' + w * '*') * c + '| ') * h + a] * r)
