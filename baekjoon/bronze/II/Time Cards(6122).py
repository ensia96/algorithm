I = input
c, n = map(int, I().split())
T = {}
for _ in ' ' * n:
    _, a, h, m = I().split()
    T[_] = T.get(_, []) + [int(h) * 60 + int(m)]
for t in sorted(T):
    w = T[t] + len(T[t]) % 2 * [1440]
    w = sum(e - s for s, e in zip(w[::2], w[1::2]))
    print(w // 60, w % 60)
