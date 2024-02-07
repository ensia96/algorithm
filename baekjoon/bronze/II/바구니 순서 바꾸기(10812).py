n, m, *A = map(int, open(0).read().split())
T = [*range(n+1)]
while A:
    i, j, k, *A = A
    T[i:j+1] = T[k:j+1]+T[i:k]
print(*T[1:])
