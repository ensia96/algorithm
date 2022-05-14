n = int(input())
A = set()
r = 0
for _ in ' '*n:
    t = input()
    if t == 'ENTER':
        r += len(A)
        A = set()
    else:
        A.add(t)
print(r+len(A))
