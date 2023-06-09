n, k = map(int, input().split())
A = [x for x in range(1, n+1)if x % 10 not in [k % 10, 2*k % 10]]
print(len(A))
print(*A)
