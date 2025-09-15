A, B = open(0)
T = [0] * 26
for a, b in zip(A[:-1], B):
    T[ord(a) - 97] += 1
    if '*' == b:
        continue
    T[ord(b) - 97] -= 1
A = B.count('*')
for i in range(26):
    A -= (T[i] > 0) * T[i]
print('NA'[A == 0])
