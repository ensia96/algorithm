n = int(input())
L, R = [0]*(n+1), [0]*(n+1)
for _ in ' '*n:
    i, l, r = [i != '.' and ord(i)-64 for i in input().split()]
    L[i], R[i] = l, r


def P(c): A.append(c) or L[c] and P(L[c]) or R[c] and P(R[c])
def I(c): L[c] and I(L[c]) or A.append(c) or R[c] and I(R[c])
def p(c): L[c] and p(L[c]) or R[c] and p(R[c]) or A.append(c)
def o(A): print(''.join(chr(s+64)for s in A))


A = []
P(1), o(A)
A = []
I(1), o(A)
A = []
p(1), o(A)
