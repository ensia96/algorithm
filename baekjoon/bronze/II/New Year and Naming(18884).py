a, b, c, _, *A = open(0)
n, m = map(int, a.split())
b, c = b.split(), c.split()
for a in A:
    a = int(a) - 1
    print(b[a % n] + c[a % m])
