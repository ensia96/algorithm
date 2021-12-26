C = set()
for _ in ' '*int(input()):
    n, f = input().split()
    if f == 'enter':
        C.add(n)
    else:
        C.remove(n)
for n in sorted(C)[::-1]:
    print(n)
