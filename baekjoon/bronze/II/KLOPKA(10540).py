(*A,) = map(int, open(0).read().split())
print(max(max(a := A[1::2]) - min(a), max(b := A[2::2]) - min(b)) ** 2)
