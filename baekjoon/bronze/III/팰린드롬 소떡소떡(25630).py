n, A = int(input()), input()
print(sum(A[i] != A[n-1-i]for i in range(n//2)))
