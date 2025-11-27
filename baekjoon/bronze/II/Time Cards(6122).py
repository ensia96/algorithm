i = int
I = input
c, n = map(i, I().split())
T = {}
C = [0] * c
for _ in ' ' * n:
    c, o, h, n = I().split()
    t = i(h) * 60 + i(n)
    if 'A' == o[2]:
        T[c] = t
    else:
        C[i(c) - 1] += t - T[c]
for c in C:
    print(c // 60, c % 60)
