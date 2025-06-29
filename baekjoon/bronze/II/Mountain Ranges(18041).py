n, m, *A = map(int, open(0).read().split())
print(max([s := 1]+[s := s*(b-a <= m)+1for a, b in zip(A, A[1:])]))
