_, *A = map(int, open(0).read().split())
c = 1
while A:
    t, *A = A
    T, A = A[:t], A[t:]
    for i in range(t-2):
        T[i+1] = min(T[i+1], (T[i]+T[i+2])/2)
    print(f"Case #{c}:", T[-2])
    c += 1
