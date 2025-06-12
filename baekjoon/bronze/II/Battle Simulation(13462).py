A = input().translate(str.maketrans('RBL', 'SKH'))
i = 0
t = ''
while i < len(A):
    x = A[i:i+3] in ["SKH", "SHK", "KSH", "KHS", "HSK", "HKS"]
    t += [A[i], 'C'][x]
    i += 1+2*x
print(t)
