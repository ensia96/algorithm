_, *L = open(0)
for I, J in zip(*[iter(L)] * 2):
    m, n = map(int, I.split())
    *A, = map(int, J.split())
    i, j = A.index(a := max(A)), 5 - 2 * a
    print(sum(0 == A[(i := i + (j := [-j, j][i + j in range(m)]))]
          for _ in '_' * n))
