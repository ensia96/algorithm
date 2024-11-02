d, *A = open(0).read().split()
n, *A = map(int, A)
D = "?15??2??8?"
A = [A[i * n : i * n + n] for i in range(n)]
for i in range(n):
    print(*[[D[int(A[-i - 1][j])], D[int(A[i][-j - 1])]][d in "LR"] for j in range(n)])
