A = input()
S = "ABCDF"
for i in "ABC":
    if i in A:
        for j in S[S.index(i) :]:
            A = A.replace(j, i)
        break
else:
    A = "A" * len(A)
print(A)
