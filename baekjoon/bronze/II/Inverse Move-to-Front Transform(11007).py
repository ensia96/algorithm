n = 0
_, *A = map(int, open(0).read().split())
while A := A[n:]:
    n, *A = A
    C = "abcdefghijklmnopqrstuvwxyz"
    print("".join((C := C[a] + C[:a] + C[a + 1 :])[0] for a in A[:n]))
