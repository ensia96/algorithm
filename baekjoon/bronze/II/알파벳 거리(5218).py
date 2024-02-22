n, *A = open(0).read().split()
for i in range(int(n)):
    print('Distances:', *[t+26*(t < 0)for t in [ord(A[i*2+1]
          [j])-ord(A[i*2][j])for j in range(len(A[i*2]))]])
