n, p, q, *A = map(int, open(0).read().split())
A = [
    x
    for a, b in zip(A[:n], A[n:])
    if (p == q and a == b or (p > q) ^ (a > b) and ((a - b) % (q - p) < 1))
    and (x := (a - b) // (q - p)) <= 10000
]
print("YNEOS"[(y := len(A) != n) :: 2])
y or print(*A)
