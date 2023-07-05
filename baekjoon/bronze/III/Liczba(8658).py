n = int(input())
for i in range(2, n):
    if n % i:
        m = i
        break
for i in range(n, 1, -1):
    if n % i:
        M = i
        break
print(m, M)
