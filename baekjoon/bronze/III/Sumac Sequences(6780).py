*A, = map(int, open(0).read().split())
while A[-2] >= A[-1] > 0:
    A += A[-2]-A[-1],
print(len(A))
