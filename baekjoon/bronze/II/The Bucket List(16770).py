T = [0] * 1001
for l in [*open(0)][1:]:
    s, t, b = map(int, l.split())
    for i in range(s, t):
        T[i] += b
print(max(T))
