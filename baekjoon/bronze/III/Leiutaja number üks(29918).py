n, m, *A = map(int, open(0).read().split())
x = 0
while A:
    a, b, *A = A
    x = max(x, a+b*10+1)
print(max(0, x-n-m*10))
