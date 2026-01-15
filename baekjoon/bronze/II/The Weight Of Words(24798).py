l, w = map(int, input().split())
w -= l
print(['impossible', ('z' * (w // 25) + chr(w %
      25 + 97) + 'a' * l)[:l]][0 <= w <= 25 * l])
