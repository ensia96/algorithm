import math
n, *A = map(float, open(0).read().split())
for i in range(int(n)):
    a, b, c = A[3*i:3*i+3]
    x, y = math.sqrt(b*b-4*a*c), 2*a
    print(f"{(-b+x)/y:.3f}, {(-b-x)/y:.3f}")
