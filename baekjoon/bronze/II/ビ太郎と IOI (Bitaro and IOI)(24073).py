n, A = open(0)
n = int(n)
print('YNeos'[all(A[i]+A[j]+A[k] != 'IOI'for i in range(n)
      for j in range(i+1, n)for k in range(j+1, n))::2])
