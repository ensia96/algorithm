A = input()
for i in range(1, len(A)):
    a, b = A[:i], A[i:]
    a == a[::-1] and b == b[::-1] and exit(print(a, b))
print('NO')
