n, k = map(int, input().split())
i = j = 0
while i < n and j < k:
    i += 1
    j += not n % i
print([i, 0][j < k])
