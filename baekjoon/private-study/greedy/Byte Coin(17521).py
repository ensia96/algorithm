n, w = map(int, input().split())
A = [int(input())for _ in ' '*n]
c = 0
for i in range(n-1):
    if A[i] < A[i+1]:
        if w//A[i] > 0:
            c, w = divmod(w, A[i])
    elif A[i] > A[i-1]:
        w, c = w+A[i]*c, 0
print(w+(c > 0)*(c*A[-1]))
