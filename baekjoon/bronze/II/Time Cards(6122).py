I = input
c, n = map(int, I().split())
C = [[]for _ in ' ' * c]
for _ in ' ' * n:
    c, a, h, m = I().split()
    C[int(c)] += int(h) * 60 + int(m),
for c in C:
    w = sum(e - s for s, e in zip(c[::2], c[1::2] + [1440]))
    print(w // 60, w % 60)
