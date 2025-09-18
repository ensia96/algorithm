A, B = open(0)
A = ''.join(map(str.upper, A[:-1])) + ' ' * 6 + A
print(''.join(b if b == ' 'else A[ord(b) - 65]for b in B[:-1]))
