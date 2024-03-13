A = input()
if 1 < len(A) and '0' == A[0]:
    A = int(A, [8, 16][A[1] == 'x'])
print(A)
