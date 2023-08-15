n, *A = open(0).read().split()
t, T = 1, ''
for i in range(int(n)):
    x = len(A[i])
    T += ' 'if x < t else A[i][t-1]
    t = x
print(T)
