n, *A = open(c := 0)
for a, b in zip(A[1::3], A[2::3]):
    c += 1
    print(f"Case {c}:", sum(a[i] != b[i] for i in range(len(a))))
