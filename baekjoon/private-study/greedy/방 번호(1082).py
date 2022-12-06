n = int(input())
*A, = map(int, input().split())
m = int(input())
if n < 2 or m < min(A[1:]):
    exit(print(0))
x, y = min((A[i], -i)for i in range(1, n))
i, j = min((A[i], -i)for i in range(n))
a, b = divmod(m-x, i)
T = [(-j, i)]*a+[(-y, x)]
R = []
while T:
    x, y = T.pop()
    for i in range(n)[::-1]:
        if A[i]-y <= b:
            b -= A[i]-y
            x = i
            break
    R += x,
print(*R, sep='')
