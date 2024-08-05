P = [10, 8, 6, 5, 4, 3, 2, 1, 0]
A = []
R = [0] * 2
for l in open(0):
    T, t = l.split()
    A += ([T, t == "B"],)
A.sort()
for i in range(8):
    R[A[i][1]] += P[i]
print("BRleude"[R[0] > R[1] :: 2])
