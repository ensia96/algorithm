N = n = int(input())
A, c = [0]*10, 1
while n:
    n, r = divmod(n, 10)
    A[0] += n*c
    for i in range(r):
        A[i+1] += (n+1)*c
    A[r] -= c-(N % c)-1
    for i in range(r+1, 10):
        A[i] += n*c
    c *= 10
print(*A)
