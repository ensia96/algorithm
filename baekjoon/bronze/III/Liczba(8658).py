n = int(input())
A = [i for i in range(2, n)if n % i]
print(min(A), max(A))
