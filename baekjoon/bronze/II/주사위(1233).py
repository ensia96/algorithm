a, b, c = map(int, input().split())
A = [0]*(a+b+c)
for i in range(a):
    for j in range(b):
        for k in range(c):
            A[i+j+k] += 1
print(A.index(max(A))+3)
