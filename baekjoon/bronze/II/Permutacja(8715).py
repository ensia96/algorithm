n, *A = map(int, open(0).read().split())
print('TNAIKE'[len({*range(1, n + 1)} - {*A}) > 0::2])
