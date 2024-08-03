A, S = [*range(4)], [0] * 4
for l in [*open(0)][1:]:
    a, b, g = map(int, l.split())
    for i in range(4):
        if A[i] == a:
            A[i] = b
        elif A[i] == b:
            A[i] = a
        S[i] += A[i] == g
print(max(S))
