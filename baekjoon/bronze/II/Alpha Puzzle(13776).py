A = ''
for i in open(0).read():
    if i.isalpha() and i not in A:
        A += i
print(A)
