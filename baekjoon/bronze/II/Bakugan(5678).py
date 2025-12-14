I = input
f = lambda: [*map(int, I().split())]
while (n := int(I())):
    M, L = f(), f()
    a, b = sum(M), sum(L)
    for i in range(n - 2):
        x, y = M[i] == M[i + 1] == M[i + 2], L[i] == L[i + 1] == L[i + 2]
        a += 30 * x
        b += 30 * y
        if x or y:
            break
    print('TML'[(a > b) + 2 * (a < b)])
