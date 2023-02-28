import math
for _ in ' '*int(input()):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(['Whole', 'Slice of'][a*d > c*c*math.pi*b], 'pizza')
