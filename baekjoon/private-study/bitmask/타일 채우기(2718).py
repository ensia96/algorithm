A, B, C = [0, 1, 5], [0, 1, 1], [0, 1, 2]
for _ in ' '*22:
    C += C[-1]+A[-1],
    B += B[-2]+A[-1],
    A += A[-2]+A[-1]+B[-2]+2*C[-2],
for _ in ' '*int(input()):
    print(A[int(input())])
