A = [i in 'yuiophjklnm'for i in input()]
print('yneos'[not all(x != y for x, y in zip(A, A[1::]))::2])
