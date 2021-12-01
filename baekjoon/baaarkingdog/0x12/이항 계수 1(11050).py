n, k = map(int, input().split())
a = b = 1
for i in range(n-k, n):
    a *= i+1
for i in range(k):
    b *= i+1
print(a//b)
