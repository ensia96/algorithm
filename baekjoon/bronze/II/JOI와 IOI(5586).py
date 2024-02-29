A = input()
x = y = 0
for i in range(len(A)-2):
    t = A[i]+A[i+1]+A[i+2]
    x += t == 'JOI'
    y += t == 'IOI'
print(x)
print(y)
