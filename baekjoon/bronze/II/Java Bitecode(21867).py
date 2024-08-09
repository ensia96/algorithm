input()
A = input()
for i in "AJV":
    A = A.replace(i, "")
print(["nojava", A][len(A) > 0])
