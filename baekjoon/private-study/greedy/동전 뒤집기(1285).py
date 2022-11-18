n = int(input())
A = [[(i == 'T', i == 'H')for i in input()]for _ in ' '*n]
a = 1 << n
for i in range(a):
    b = 0
    for x in range(n):
        t = sum(A[y][x][bool((1 << y) & i)]for y in range(n))
        b += min(t, n-t)
    a = min(a, b)
print(a)
