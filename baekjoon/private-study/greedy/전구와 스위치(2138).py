def f(x):
    if x[i-1] == B[i-1]:
        return 0
    for j in range(3):
        k = i+j-1
        if k < n:
            x[k] = not x[k]
    return 1


n = int(input())
*A, = map(int, input())
a = A[::]
*B, = map(int, input())
for i in range(2):
    a[i] = not a[i]
T, t = 0, 1
for i in range(1, n):
    T += f(A)
    t += f(a)
x, y = a == B, A == B
print(min(t, T)if x*y else t if x else T if y else -1)
