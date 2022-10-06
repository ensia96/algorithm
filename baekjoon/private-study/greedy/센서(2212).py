n = int(input())
k = int(input())
A = sorted(map(int, input().split()))
A = sorted(A[i+1]-A[i]for i in range(n-1))
while A and k > 1:
    A.pop()
    k -= 1
print(sum(A))
