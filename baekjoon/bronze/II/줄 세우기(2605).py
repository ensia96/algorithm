n, *A = map(int, open(0).read().split())
l = []
for i in range(n):
    a = A[i]
    l = l[:a]+[i+1]+l[a:]
print(*l[::-1])
