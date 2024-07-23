f = lambda: map(int, input().split())
n, q = f()
A = [0, *f()]
for _ in " " * q:
    _, *C = f()
    if _ < 2:
        a, b = C
        print(sum(A[a : b + 1]))
        A[a], A[b] = A[b], A[a]
    else:
        a, b, c, d = C
        print(sum(A[a : b + 1]) - sum(A[c : d + 1]))
