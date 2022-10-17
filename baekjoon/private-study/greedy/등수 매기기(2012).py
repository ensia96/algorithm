n = int(input())
A = sorted(int(input())for _ in ' '*n)
print(sum(abs(A[i]-i-1)for i in range(n)))
