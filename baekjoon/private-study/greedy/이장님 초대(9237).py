n = int(input())
A = sorted(map(int, input().split()))[::-1]
print(max(2+i+A[i]for i in range(n)))
