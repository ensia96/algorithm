I, R = input, range
T, W = map(int, I().split())
D = [[[0] * (W + 1) for _ in R(2)] for _ in R(T + 1)]
for t in R(T):
    p = int(I()) == 1
    for w in R(W + 1):
        D[t][0][w] = max(D[t - 1][0][w], w < W and D[t - 1][1][w + 1]) + p
        D[t][1][w] = max(D[t - 1][1][w], w < W and D[t - 1][0][w + 1]) + (not p)
print(max(map(max, map(max, D))))
