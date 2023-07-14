_, *L = map(int, open(0).read().split())
S = L[1::2]
s = S.index(max(S))
print(+(S[s] in [1, 4]) and L[::2][s]+20*s)
