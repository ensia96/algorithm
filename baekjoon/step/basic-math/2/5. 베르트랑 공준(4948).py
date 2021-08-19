l = map(int, [*open(0)][:-1])
a = 2 * max(l) + 2
b = [1 for _ in range(a)]

for i in range(2, int(a ** 0.5) + 1):
    if b[i]:
        for j in range(2 * i, a, i):
            b[i] = 0

for n in l:
    print(sum(b[i] for i in range(n, 2 * n + 1) if i > 1))
