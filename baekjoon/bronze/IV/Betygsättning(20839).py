x, y, z = map(int, input().split())
a, b, c = map(int, input().split())
print('E'if c < z or 2*b < y else 'D'if b <
      y else 'C'if 2*a < x else 'B'if a < x else 'A')
