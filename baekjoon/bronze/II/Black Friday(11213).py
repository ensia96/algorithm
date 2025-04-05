(*A,) = map(int, open(0).read().split()[1:])
for a in sorted(A)[::-1]:
    if A.count(a) < 2:
        exit(print(A.index(a) + 1))
print("none")
