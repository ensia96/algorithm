n, k = map(int, input().split())
A = input()
T = [A[0]]
for i in range(1, n):
    while k and T and T[-1] < A[i]:
        T.pop()
        k -= 1
    T += A[i],
while k:
    T.pop()
    k -= 1
print(''.join(T))
