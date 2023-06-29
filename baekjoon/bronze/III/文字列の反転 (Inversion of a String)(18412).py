n, a, b = map(int, input().split())
A = input()
print(A[:a-1]+A[b-1:a-2:-1]+A[b:])
