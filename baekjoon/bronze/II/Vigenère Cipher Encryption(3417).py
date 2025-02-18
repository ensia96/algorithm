*A, _ = open(0)
for a, b in zip(A[::2], A[1::2]):
    print(
        "".join(
            chr((ord(b[i]) + ord(a[i % ~-len(a)]) - 129) % 26 + 65)
            for i in range(len(b) - 1)
        )
    )
