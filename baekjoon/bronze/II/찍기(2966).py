n, A = open(0)
T = [sum(A[j] == B[j % len(B)]for j in range(int(n)))
     for B in ['ABC', 'BABC', 'CCAABB']]
x = max(T)
print(x)
for i in range(3):
    x-T[i] or print(['Adrian', 'Bruno', 'Goran'][i])
