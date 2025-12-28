input()
A = input().split()
print('NTIAEK'[any(a != b and b != c and a !=
      c for a, b, c in zip(A, A[1:], A[2:]))::2])
