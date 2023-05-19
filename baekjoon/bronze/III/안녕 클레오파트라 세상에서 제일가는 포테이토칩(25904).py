n, x = map(int, input().split())
*A, = map(int, input().split())
i = 0
while A[i % n] >= x+i:
    i += 1
print(i % n+1)
