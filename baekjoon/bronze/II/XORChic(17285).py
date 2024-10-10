(*A,) = map(ord, input())
print("".join(chr(67 ^ A[0] ^ a) for a in A))
