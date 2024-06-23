a, b, c, d = map(lambda x: 'SPR'.find(x), input().split())
print([['?', 'MS'][c == d and (c+2) % 3 in [a, b]], 'TK']
      [a == b and (a+2) % 3 in [c, d]])
