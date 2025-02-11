import math

for l in [*open(0)][1:]:
    a, _, b = l.split()
    x = a != "H"
    print(14 * x + (2 * x - 1) * math.log10(float(b)))
