t = 'Present!'
n, *A = open(0).read().split()
for a in sorted(A[i]for i in range(int(n))if t not in A[i:i+2]) or ['No Absences']:
    print(a)
