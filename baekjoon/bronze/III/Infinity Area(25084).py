import math
i = 1
for l in [*open(0)][1:]:
    a, b, c = map(int, l.split())
    t = p = 0
    while a > 0:
        t += a*a
        a = [a*b, a//c][p]
        p = -~p % 2
    print(f'Case #{i}:', t*math.pi)
    i += 1
