for l in [*open(0)][:-1]:
    _, N, _ = l.split()
    len(T := {i for i, j in zip(N, N[1:])if i == j}) and print(
        ' and '.join(f'{t} {t} glued'for t in sorted(T)))
