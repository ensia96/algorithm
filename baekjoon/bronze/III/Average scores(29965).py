n, *A, = map(int, open(0).read().replace(*'M0').replace(*'J1').split())
A, B = A[::2], A[1::2]
T = [0]*2
for i in range(n):
    T[A[i]] += B[i]
x, y = T[0]/(A.count(0) or 1), T[1]/(A.count(1) or 1)
print('VMJ'[(x > y)+2*(x < y)])
