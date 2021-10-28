I, R = input, range
T, W = map(int, I().split())
P = [int(I()) for _ in R(T)]
D = [[0] * (W + 1) for _ in range(T)]
for t in R(T):
    p = P[t] == 1
    D[t][0] = D[t - 1][0] + p
    for w in R(1, W + 1):
        a = bool((p * (not w % 2)) + ((not p) * (w % 2)))
        D[t][w] = max(D[t - 1][w], D[t - 1][w - 1]) + a
print(max(D.pop()))
