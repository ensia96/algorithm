A = input()
i = 0
n = len(A)
while i < n:
    x = i+2 < n and A[i] != A[i+1] != A[i+2]
    print(['SKH'['RBL'.find(A[i])], 'C'][x], end='')
    i += 1+2*x
