A = input()
B = input()
n, m = len(A), len(B)
i = c = 0
while i < n:
    k = 0
    for j in range(m):
        if i+k >= n or A[i+k] != B[j]:
            break
        k += 1
    else:
        c += 1
        i += m-1
    i += 1
print(c)
