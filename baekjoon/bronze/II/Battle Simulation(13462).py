A = input()
i = len(A)
t = ''
while i > 0:
    x = i > 2 and A[-i] != A[-i+1] != A[-i+2]
    t += ['SKH'['RBL'.index(A[-i])], 'C'][x]
    i -= 1+2*x
print(t)
