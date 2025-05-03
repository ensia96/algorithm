_, k = map(int, input().split())
A = input()
print(A[:k-1]+A[k-1:].swapcase())
