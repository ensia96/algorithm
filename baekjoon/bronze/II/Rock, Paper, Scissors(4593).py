*I, _, _ = open(0)
for A, B in zip(I[::2], I[1::2]):
    a = b = 0
    for i in range(len(A)):
        x = A[i] + B[i]
        a += x in ["RS", "SP", "PR"]
        b += x in ["SR", "PS", "RP"]
    print("P1:", a)
    print("P2:", b)
