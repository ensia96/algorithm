A = input()
i = len(A)
while i > 0:
    x = i > 2 and (A[-i] != A[-i+1] != A[-i+2])
    print(['SKH'['RBL'.index(A[-i])], 'C'][x], end='')
    i -= 1+2*x
