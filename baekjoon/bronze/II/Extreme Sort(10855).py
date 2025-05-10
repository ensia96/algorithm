*A, = map(int, [*open(0)][1].split())
print('yneos'[any(a != b for a, b in zip(A, sorted(A)))::2])
