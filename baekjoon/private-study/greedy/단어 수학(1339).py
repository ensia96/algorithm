n = int(input())
D = {}
for _ in ' '*n:
    S = input()
    for i in range(len(S)):
        D[S[i]] = D.get(S[i], 0)+10**(len(S)-i-1)
print(sum(D[j]*(9-i)for i, j in enumerate(sorted(D, key=lambda x: -D[x]))))
