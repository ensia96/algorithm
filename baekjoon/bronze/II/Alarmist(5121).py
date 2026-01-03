f = lambda: map(int, input().split())
A = []
for t in range(*f()):
    n, w = f()
    *S, = f()
    S = sorted(sum(S[i:i + w]) // w for i in range(n - w + 1))
    A += f"Data Set {t + 1}:\n{S[-1] - S[0]}",
print(*A, sep="\n\n")
