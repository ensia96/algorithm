A = sorted(int(input())for _ in ' '*int(input()))[::-1]
print(sum(A)-sum(A[2::3]))
