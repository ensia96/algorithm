A = input()
for i in input().split():
    A = A.replace(i, chr(ord(i)+32))
print(A)
