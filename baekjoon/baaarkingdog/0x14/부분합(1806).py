n, s = map(int, input().split())
A = [*map(int, input().split())]
a, c, j = 2**17, A[0], 1
for i in range(n):
    while j < n and c < s:
        c, j = c+A[j], j+1
    if c >= s:
        a = min(a, j-i)
    c -= A[i]
print(0 if a == 2**17 else a)
