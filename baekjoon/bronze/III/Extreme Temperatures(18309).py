A = [int(i)for i in open(0).read().split()if '-'not in i]
print(min(A), max(A))
