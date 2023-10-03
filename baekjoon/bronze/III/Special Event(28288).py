A = [i.count('Y')for i in zip(*[input()for _ in ' '*int(input())])]
print(','.join([str(-~i)for i, j in enumerate(A)if j == max(A)]))
