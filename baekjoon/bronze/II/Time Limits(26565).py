_, *L = open(0)
for A, T in zip(L[::2], L[1::2]):
    n, s = map(int, A.split())
    M = max(map(int, T.split()))
    print(s * M // 1000 + (M % 1000 > 0))
