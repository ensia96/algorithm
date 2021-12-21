n, s = map(int, input().split())
A = [*map(int, input().split())]
a, c, j = 2**17, A[0], 0
for i in range(n):
    while j < n and c < s:
        j += 1
        if j != n:
            c += A[j]
    if j == n:
        break
    a, c = min(a, j-i+1), c-A[i]
print(0 if a == 2**17 else a)
