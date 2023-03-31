p, k = map(int, input().split())
M = 1000001
A = [1]*M
for i in range(2, 1001):
    if A[i]:
        for j in range(2*i, M, i):
            A[j] = 0
for i in range(2, k):
    A[i] and (p % i or exit(print('BAD', i)))
print("GOOD")
