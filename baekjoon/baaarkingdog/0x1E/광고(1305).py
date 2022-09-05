L = int(input())
A = input()
f, j = [0]*L, 0
for i in range(1, L):
    while j and A[i] != A[j]:
        j = f[j-1]
    if A[i] == A[j]:
        j += 1
        f[i] = j
print(L-f[-1])
