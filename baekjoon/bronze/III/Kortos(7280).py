*A, = open(0).read().split()
*B, = map(int, A[1::2])
print(*[i for i in 'SBVK'if A.count(i) < 13], *
      [i for i in range(1, 14)if B.count(i) < 4])
