n = int(input())
*A, = map(int, input().split())
s = int(input())
for i in range(n-1):
    x, y = A[i], i
    for j in range(i+1, min(i+1+s, n)):
        if A[j] > x:
            x, y = A[j], j
    if y-i:
        A = A[:i]+A[y:y+1]+A[i:y]+A[y+1:]
        s -= y-i
print(*A)
