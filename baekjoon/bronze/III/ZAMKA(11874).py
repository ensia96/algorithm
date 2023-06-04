l, d, x = map(int, open(0))
A = []
for i in range(l, d+1):
    t = sum(map(int, str(i)))
    if t == x:
        A += i,
print(A[0])
print(A[-1])
