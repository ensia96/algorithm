A = input()
print(10+sum(5+5*(A[i+1] != A[i])for i in range(len(A)-1)))
