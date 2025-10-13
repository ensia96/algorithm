n, x, *A = map(int, open(0).read().split())
T = [x]
for a in A:
    if x < a:
        T += a,
        x = a
print(len(T))
print(*T)
