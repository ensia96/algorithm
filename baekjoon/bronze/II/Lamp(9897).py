I = input
n, m, k = map(int, I().split())
P = {}
C = [0] * n
for _ in ' ' * m:
    g, *A = I().split()
    s, c = map(int, A)
    P[g] = s - 1, n, c,
for _ in ' ' * k:
    for i in range(*P[I()]):
        C[i] ^= 1
print(sum(C))
