l = [*open(0)][:-1]
a = max(l) + 1
b = [1 for _ in range(a)]

for i in range(2, int(a ** 0.5) + 1):
    if b[i]:
        for j in range(2 * i, a, i):
            b[i] = 0

for n in l:
    sum(1 if i > 1 and b[i] else 0 for i in range(n, 2 * n + 1))
