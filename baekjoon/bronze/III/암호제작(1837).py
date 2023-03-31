p, k = map(int, input().split())
k += 1
A = [1]*k
for i in range(2, int(k**.5)+1):
    if A[i]:
        for j in range(2*i, k, i):
            A[j] = 0
for i in range(2, k):
    A[i] and p % i or exit(print('BAD', i))
print('GOOD')
