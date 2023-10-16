n = int(input())//10
A = input()
print(sum(n == A[i*n:n*-~i].count('T')for i in range(10)))
