T = input()
P = input()
f, j = [0]*len(P), 0
for i in range(1, len(P)):
    while j and P[i] != P[j]:
        j = f[j-1]
    if P[i] == P[j]:
        j += 1
        f[i] = j
A = j = 0
L = []
for i in range(len(T)):
    while j and T[i] != P[j]:
        j = f[j-1]
    j += T[i] == P[j]
    if j == len(P):
        L += i-j+2,
        j = f[j-1]
        A += 1
print(A)
for l in L:
    print(l)
