(*A,) = map(int, input().split())
x, y = (A[x := A.index(20)] + A[x - 1] + A[-~x % 20]) / 3, sum(A) / 20
print(["TBioeb"[x < y :: 2], "Alice"][x > y])
