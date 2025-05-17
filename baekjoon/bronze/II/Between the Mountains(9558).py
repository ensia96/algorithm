_, *A = open(0)
for A, B in zip(A[::2], A[1::2]):
    print(min(abs(a-b)for a in [*map(int, A.split())][1:]
          for b in [*map(int, B.split())][1:]))
