import string
for _ in ' '*int(input()):
    S = input()
    print(sum((i not in S)*ord(i)for i in string.ascii_uppercase))
