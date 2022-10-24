n, k = map(int, input().split())
A = [*input()]
c = 0
for i in range(n):
    if A[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0 <= j < n and A[j] == 'H':
                A[j] = 'h'
                c += 1
                break
print(c)
