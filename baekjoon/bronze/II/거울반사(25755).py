d, n, *A = open(0).read().split()
n = int(n)
D = "?15??2??8?"
for i in range(n):
    print(
        *[
            [D[int(A[(-i - 1) * n + j])], D[int(A[i * n - j - 1])]][d in "LR"]
            for j in range(n)
        ]
    )
