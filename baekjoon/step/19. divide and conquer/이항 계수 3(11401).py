M = 1000000007
n, k = map(int, input().split())


def f(x):
    A = 1
    for i in range(x):
        A = A*(i+1) % M
    return A


x, y = f(k)*f(n-k) % M, M-2
A = 1
while y > 0:
    if y % 2:
        A = (A*x) % M
    x, y = x*x % M, y//2
print(f(n)*A % M)
