t, _, *A = map(int, open(0).read().split())
print('Padaeng_i', ['Happy', 'Cry'][sum(A) < t])
