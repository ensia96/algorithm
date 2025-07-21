print(A := ''.join(map(str.lower, input())))
for i in range(len(A)-1):
    A[i] == A[i+1] == 's' and print(A[:i]+'B'+A[i+2:])
