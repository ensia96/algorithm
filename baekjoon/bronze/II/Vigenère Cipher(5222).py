for l in [*open(0)][1:]:
    A, B = l.split()
    print('Ciphertext:', ''.join(
        chr((ord(B[i]) + ord(A[i % len(A)]) - 130) % 26 + 65)for i in range(len(B))))
