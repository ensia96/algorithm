a, b, c = map(int, input().split())
print(['OK', {a: 'Soongsil', b: 'Korea', c: 'Hanyang'}
      [min(a, b, c)]][a+b+c < 100])
