g, I = lambda a, b: b*(a == 0) or g(b % a, a), input
n = int(I())
A = I().split()
B = I().split()
B += B
f, j = [0]*n, 0
for i in range(1, n):
    while j and A[i] != A[j]:
        j = f[j-1]
    if A[i] == A[j]:
        j += 1
        f[i] = j
j = c = 0
for i in range(1, n*2):
    while j and B[i] != A[j]:
        j = f[j-1]
    j += B[i] == A[j]
    if j == n:
        j = f[j-1]
        c += 1
g = g(n, c)
print(f"{c//g}/{n//g}"if g else f"{c}/{n}")
