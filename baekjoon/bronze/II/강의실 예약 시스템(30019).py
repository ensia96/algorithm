n, m, *A = map(int, open(0).read().split())
T = [0] * -~n
for a, b, c in zip(*[iter(A)] * 3):
    if T[a] <= b:
        T[a] = c
    print("YNEOS"[T[a] > b :: 2])
