I, R = input, range
T, W = map(int, I().split())
D = [[[0] * (W + 1) for _ in R(2)] for _ in R(T + 1)]
p = int(I()) == 1
D[0][0][W], D[0][1][W - 1] = p, not (p)
for t in R(1, T):
    p = int(I()) == 1
    for w in R(W + 1):
        D[t][0][w] = max(D[t - 1][0][w], w < W and D[t - 1][1][w + 1]) + p
        D[t][1][w] = max(D[t - 1][1][w], w < W and D[t - 1][0][w + 1]) + (not p)
print(max(map(max, map(max, D))))
