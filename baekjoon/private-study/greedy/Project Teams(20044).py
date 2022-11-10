n = int(input())
A = sorted(map(int, input().split()))
print(min(A[i]+A[-i-1]for i in range(n)))
