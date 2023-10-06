D, R = {}, ''
for _ in ' '*int(input()):
    a, b = input().split()
    D[b] = a
A = input()
for i in range(len(A)//4):
    t = A[i*4:-~i*4]
    R += D[t]if t in D else '?'
print(R)
