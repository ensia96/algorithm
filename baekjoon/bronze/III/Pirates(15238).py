input()
A = input()
print(*max((A.count(a), a)for a in A)[::-1])
