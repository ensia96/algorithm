n = int(input())
A = [*map(int, input().split())]
D, d = [1]*n, [1]*n
for i in range(1, n):
    D[i] = 1+(A[i] >= A[i-1])*D[i-1]
    d[-i-1] = 1+(A[-i-1] >= A[-i])*d[-i]
print(max(D+d))
