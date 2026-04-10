input()
B = sorted(A := input().split(), key=int)
for a in A:
    i = B.index(a)
    print(i + 1, end=" ")
    B[i] = 0
