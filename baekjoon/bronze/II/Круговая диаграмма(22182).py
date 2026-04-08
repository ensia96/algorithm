_, r, *A = map(int, open(0).read().split())
for a in A:
    print(3.1415926535 * r * r * a / sum(A))
