T = sorted(sorted([abs(a - c), abs(b - d)])
           for a, b, c, d in (map(int, l.split())for l in [*open(0)][1:]))
print(sum((p > q) | (r > s)for i, (p, r) in enumerate(T)for q, s in T[i + 1:]))
