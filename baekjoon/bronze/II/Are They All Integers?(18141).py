n, *A = map(int, open(0).read().split())
N = range(n)
print(
    "yneos"[
        any(
            (A[i] - A[j]) % A[k]
            for i in N
            for j in N
            for k in N
            if i != j and j != k and k != i
        ) :: 2
    ]
)
