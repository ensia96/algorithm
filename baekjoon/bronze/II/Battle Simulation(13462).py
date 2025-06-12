A = input()
i = 0
while i < len(A):
    x = len(set(A[i:i+3])) == 3
    print(['SKH'['RBL'.find(A[i])], 'C'][x], end='')
    i += 1+2*x
