f, R = lambda a, b: b*(a == 0) or f(b % a, a), range,
n, *A = map(int, open(0).read().split())
x = f(A[0], A[1])
if n > 2:
    x = f(x, A[2])
for i in range(x):
    x % -~i or print(-~i)
