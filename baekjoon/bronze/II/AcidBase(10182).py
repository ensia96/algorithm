import math

for _ in " " * int(input()):
    a, _, b = input().split()
    x = a != "H"
    print(f"{14*x+(2*x-1)*math.log10(float(b)):0.2f}")
