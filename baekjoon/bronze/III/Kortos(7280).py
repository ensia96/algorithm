*A, = open(0).read().split()
print(*[i for i in 'SBVK'if A.count(i) < 13], *
      [i for i in range(14)if A.count(str(i)) < 4])
