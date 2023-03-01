A, x = input(), 0
while x < len(A):
    x, y = x+1, ord(A[x])-65
    A = A[:x]+A[x+y:]
print(A)
