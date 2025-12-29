R = []
for t in range(int(input())):
    n, m, *C = map(int, input().split())
    for A in zip(*[input()for _ in '_' * n]):
        f = 1
        C += ['N', sum(f * (3 * (a == 'H') + (a == 'S'))
                       for a in A if (f := f and a != 'X'))]['X' in A],
    R += f"Data Set {t + 1}:\n" + ' '.join(map(str, C)),
print('\n\n'.join(R))
