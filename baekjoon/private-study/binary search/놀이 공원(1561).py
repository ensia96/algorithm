n, m = map(int, input().split())
A = [*map(int, input().split())]
l, r = 0, max(A)*n
while l <= r:
    t = (l+r)//2
    if m+sum(t//a for a in A) < n:
        l = t+1
    else:
        r = t-1
x = n-m-sum((l-1)//a for a in A)
for i in range(m):
    x -= not l % A[i]
    x or exit(print(i+1))
