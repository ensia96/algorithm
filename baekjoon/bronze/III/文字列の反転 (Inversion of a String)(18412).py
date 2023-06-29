n, a, b = map(int, input().split())
A = input()
print(A[:a-1]+A[a-1:b][::-1]+A[b:])
