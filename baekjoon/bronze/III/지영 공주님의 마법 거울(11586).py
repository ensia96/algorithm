n, *A, k = map(str.strip, [*open(0)])
print('\n'.join([A, [a[::-1]for a in A], A[::-1]][int(k)-1]))
