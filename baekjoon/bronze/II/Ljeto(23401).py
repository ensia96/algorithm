S = [0] * 2
T = [-9] * 9
for l in [*open(0)][1:]:
    t, a, _ = map(int, l.split())
    S[a > 4] += 100 + (t < T[a] + 11) * 50
    T[a] = t
print(*S)
