a, b = map(int, input().split())
A = [*zip(map(int, bin(a)[2:].zfill(9)[::-1]),
          map(int, bin(b)[2:].zfill(9)[::-1]))]
print(sum(2**i*(sum(A[i]) == 1)for i in range(9)))
