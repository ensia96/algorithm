F = [1] * 2
for i in range(44):
    F += (F[-2] + F[-1],)
for i in map(int, [*open(0)][1:]):
    print(F[i])
