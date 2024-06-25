S, t, *A = open(0).read().split()
S = [*S]
for i in range(int(t)):
    a, b = map(int, A[2*i:2*i+2])
    S[a], S[b] = S[b], S[a]
print(''.join(S))
