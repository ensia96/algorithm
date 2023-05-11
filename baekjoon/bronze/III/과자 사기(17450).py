a, b, c, d, e, f = map(int, open(0).read().split())
print('SNU'[max((b*10/a*10-500*(a > 499), 0), (d*10/c*10 -
      500*(c > 499), 1), (f*10/e*10-500*(e > 499), 2))[-1]])
