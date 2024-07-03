n, p = map(int, input().split())
x = 1
for i in range(2, n + 1):
    x = x * i % p
print(x)
