n, *A = open(0).read().split()
for i in range(int(n)):
    n, *A = A
    n = int(n)+1
    T, A = A[:n], A[n:]
    S, *T = T
    print(f"Data Set {i+1}:\n{sum(any(s in t for s in S)for t in T)}\n")
