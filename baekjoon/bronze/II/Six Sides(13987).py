(*A,) = map(int, open(0).read().split())
print(
    f"{sum(a>b for a in A[:6]for b in A[6:])/(36-sum(a==b for a in A[:6]for b in A[6:])):.5f}"
)
