n, *A = open(0)
for i in range(int(n)):
    a, b = A[2*i:2*i+2]
    print(''.join(c if c == ' 'else b[ord(c)-65]for c in a[:-1]))
