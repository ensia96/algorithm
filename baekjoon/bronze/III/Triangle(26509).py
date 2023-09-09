for _ in ' '*int(input()):
    a, b, c = sorted(map(int, input().split()))
    d, e, f = sorted(map(int, input().split()))
    print('YNEOS'[not (a*a+b*b == c*c == d*d+e*e == f*f and (a ==
          d and b == e or a == e and b == e) and c == f)::2])
