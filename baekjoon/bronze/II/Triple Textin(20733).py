A = input()
n = len(A)//3
print(max([A[i*n:i*n+n]for i in range(3)], key=A.count))
