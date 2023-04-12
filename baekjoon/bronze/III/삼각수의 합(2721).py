A, B = [0], [0]
for i in range(301):
    A += A[i]+i+1,
for i in range(300):
    B += B[i]+A[i+1]*(i),
for l in [*open(0)][1:]:
    print(B[int(l)+1])
