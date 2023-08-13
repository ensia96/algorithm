a, b, c, d, e = map(int, open(0).read().split())
print(a == b == c == d or a+e == b == c == d or a == b+e ==
      c == d or a == b == c+e == d or a == b == c == d+e)
