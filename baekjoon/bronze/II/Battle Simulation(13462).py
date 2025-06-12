A = input().translate(str.maketrans('RBL', 'SKH'))
for t in ["SKH", "SHK", "KSH", "KHS", "HSK", "HKS"]:
    A = A.replace(t, 'C')
print(A)
