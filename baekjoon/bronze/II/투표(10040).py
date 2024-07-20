n, _, *A = map(int, open(0).read().split())
S = [0] * n
for s in A[n:]:
    for i in range(n):
        if A[i] <= s:
            S[i] += 1
            break
print(S.index(max(S)) + 1)
