n = int(input())
A = [n]
while n > 1:
    n = [n//2, 3*n+1][n % 2]
    A += n,
print(*A)
