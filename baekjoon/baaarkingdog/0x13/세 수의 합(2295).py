import sys
I = sys.stdin.readline
n = int(I())
U = sorted(int(I())for _ in ' '*n)
S = sorted(U[i]+U[j] for i in range(n)for j in range(i, n))
L, A = len(S), 0
for i in range(n)[::-1]:
    for j in range(i):
        v = U[i]-U[j]
        if U[i] > A:
            s, e, f = 0, L-1, 0
            while s <= e:
                m = (s+e)//2
                if S[m] == v:
                    f = 1
                    break
                elif S[m] > v:
                    e = m-1
                else:
                    s = m+1
            if f:
                A = U[i]
print(A)
