_, S, *A = open(0)
*S, = map(int, S.split())
for a in A:
    a, b, c = map(int, a.split())
    b -= 1
    if a > 1:
        S[b:c] = [[i ^ 1, 0, 1][a-2]for i in S[b:c]]
    else:
        S[b] = c
print(*S)
